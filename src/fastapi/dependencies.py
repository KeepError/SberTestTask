from typing import Annotated

from fastapi import Depends

from src.domain.repositories import UnitOfWork
from src.domain.services import VisitedLinksService
from src.infrastructure.postgres.repositories import PostgresUnitOfWork


def get_uow() -> type[UnitOfWork]:
    return PostgresUnitOfWork


def get_visited_links_service(uow: Annotated[type[UnitOfWork], Depends(get_uow)]) -> VisitedLinksService:
    return VisitedLinksService(uow=uow)
