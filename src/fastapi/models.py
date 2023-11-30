from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: str = "ok"


class AddVisitedLinksRequest(BaseModel):
    links: list[str]


class AddVisitedLinksResponse(BaseResponse):
    pass


class GetVisitedDomainsRequest(BaseModel):
    from_time: int
    to_time: int


class GetVisitedDomainsResponse(BaseResponse):
    domains: list[str]
