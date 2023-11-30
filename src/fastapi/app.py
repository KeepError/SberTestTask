import asyncio

from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError

from src.infrastructure.postgres.setup import setup_postgres
from .errors import request_validation_error_handler
from .routers import visited_links_router


async def setup():
    await setup_postgres()


def get_app() -> FastAPI:
    app = FastAPI()

    app.include_router(visited_links_router)

    app.add_exception_handler(RequestValidationError, request_validation_error_handler)

    return app


loop = asyncio.get_running_loop()
loop.create_task(setup())
fastapi_app = get_app()
