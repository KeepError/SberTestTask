from src.domain.repositories import UnitOfWork
from src.domain.services import VisitedLinksService
from src.infrastructure.in_memory_database.repositories import InMemoryUnitOfWork


def get_uow() -> type[UnitOfWork]:
    return InMemoryUnitOfWork


def get_visited_links_service() -> VisitedLinksService:
    return VisitedLinksService(uow=get_uow())
