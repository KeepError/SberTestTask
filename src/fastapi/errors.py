from enum import Enum

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse


class Error(Enum):
    VALIDATION = "validation_error"


def error_response(status_code: int, status: Error, details) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"status": status.value, "details": details}
    )


def request_validation_error_handler(request: Request, exc: RequestValidationError):
    return error_response(
        status_code=422,
        status=Error.VALIDATION,
        details=exc.errors()
    )
