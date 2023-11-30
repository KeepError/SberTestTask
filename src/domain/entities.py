import uuid
from datetime import datetime

from pydantic import BaseModel


class VisitedLink(BaseModel):
    visited_link_id: uuid.UUID
    url: str
    time: datetime
