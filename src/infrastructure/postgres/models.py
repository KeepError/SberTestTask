import uuid
from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities import VisitedLink
from .database import Base


class VisitedLinkModel(Base):
    __tablename__ = 'visited_links'

    visited_link_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    url: Mapped[str] = mapped_column(String, nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    @staticmethod
    def from_entity(entity: VisitedLink) -> 'VisitedLinkModel':
        return VisitedLinkModel(
            visited_link_id=entity.visited_link_id,
            url=entity.url,
            time=entity.time,
        )

    def to_entity(self) -> VisitedLink:
        return VisitedLink(
            visited_link_id=self.visited_link_id,
            url=self.url,
            time=self.time,
        )
