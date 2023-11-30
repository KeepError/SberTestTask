from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.domain.services import VisitedLinksService, FromTimeGreaterThanToTimeError
from . import models
from .dependencies import get_visited_links_service
from .errors import Error, error_response

visited_links_router = APIRouter(tags=["visited_links"])


@visited_links_router.post("/visited_links", response_model=models.AddVisitedLinksResponse)
async def add_visited_links(
        visited_links_service: Annotated[VisitedLinksService, Depends(get_visited_links_service)],
        request_data: models.AddVisitedLinksRequest,
):
    await visited_links_service.add_visited_urls(request_data.links)
    return models.AddVisitedLinksResponse()


@visited_links_router.get("/visited_domains",
                          response_model=models.GetVisitedDomainsResponse)
async def get_visited_domains(
        visited_links_service: Annotated[VisitedLinksService, Depends(get_visited_links_service)],
        from_time_ts: int = Query(alias="from"),
        to_time_ts: int = Query(alias="to"),
):
    from_time = datetime.fromtimestamp(from_time_ts)
    to_time = datetime.fromtimestamp(to_time_ts)
    try:
        visited_domains = await visited_links_service.get_visited_domains(from_time=from_time, to_time=to_time)
    except FromTimeGreaterThanToTimeError:
        return error_response(
            status_code=422,
            status=Error.VALIDATION,
            details="Start time must be less than end time",
        )
    return models.GetVisitedDomainsResponse(domains=visited_domains)
