from datetime import datetime
from urllib.parse import urlparse

from .repositories import UnitOfWork


class VisitedLinksService:
    uow: type[UnitOfWork]

    def __init__(self, uow: type[UnitOfWork]):
        self.uow = uow

    @staticmethod
    def _get_domain(url: str) -> str:
        return urlparse(url).netloc

    async def add_visited_urls(self, urls: list[str]) -> None:
        time = datetime.now()
        async with self.uow() as uow:
            for url in urls:
                await uow.visited_links.add_visited_url(url=url, time=time)

    async def get_visited_domains(self, from_time: datetime, to_time: datetime) -> list[str]:
        if from_time > to_time:
            raise FromTimeGreaterThanToTimeError()
        async with self.uow() as uow:
            visited_urls = await uow.visited_links.get_visited_urls(from_time=from_time, to_time=to_time)
        visited_domains = [self._get_domain(url) for url in visited_urls]
        return list(set(visited_domains))


class DomainError(Exception):
    pass


class FromTimeGreaterThanToTimeError(DomainError):
    pass
