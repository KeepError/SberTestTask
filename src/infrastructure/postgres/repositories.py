import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories import VisitedLinksRepository, UnitOfWork
from .database import SessionLocal
from .models import VisitedLinkModel


class PostgresVisitedLinksRepository(VisitedLinksRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_visited_url(self, url: str, time: datetime) -> None:
        visited_link = VisitedLinkModel(visited_link_id=uuid.uuid4(), url=url, time=time)
        self.session.add(visited_link)

    async def get_visited_urls(self, from_time: datetime, to_time: datetime) -> list[str]:
        result = await self.session.execute(
            select(VisitedLinkModel).filter(VisitedLinkModel.time.between(from_time, to_time))
        )
        visited_links = result.scalars().all()
        return [visited_link.url for visited_link in visited_links]


class PostgresUnitOfWork(UnitOfWork):
    visited_links: VisitedLinksRepository

    async def __aenter__(self) -> 'UnitOfWork':
        self.session = SessionLocal()
        self.visited_links = PostgresVisitedLinksRepository(session=self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            await self.session.commit()
        else:
            await self.session.rollback()
        await self.session.close()
