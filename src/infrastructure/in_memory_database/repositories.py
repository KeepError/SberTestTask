from datetime import datetime

from src.domain.repositories import VisitedLinksRepository, UnitOfWork

visited_links = []


class InMemoryVisitedLinksRepository(VisitedLinksRepository):
    async def add_visited_url(self, url: str, time: datetime) -> None:
        visited_links.append({"url": url, "time": time})

    async def get_visited_urls(self, from_time: datetime, to_time: datetime) -> list[str]:
        return [visited_link["url"] for visited_link in visited_links if from_time <= visited_link["time"] <= to_time]


class InMemoryUnitOfWork(UnitOfWork):
    visited_links: VisitedLinksRepository

    async def __aenter__(self) -> 'UnitOfWork':
        self.visited_links = InMemoryVisitedLinksRepository()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return None
