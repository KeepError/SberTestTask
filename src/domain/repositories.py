from abc import ABC, abstractmethod
from datetime import datetime


class VisitedLinksRepository(ABC):
    @abstractmethod
    async def add_visited_url(self, url: str, time: datetime) -> None:
        pass

    @abstractmethod
    async def get_visited_urls(self, from_time: datetime, to_time: datetime) -> list[str]:
        pass


class UnitOfWork(ABC):
    visited_links: VisitedLinksRepository
