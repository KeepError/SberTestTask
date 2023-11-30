from .database import Base, engine


# noinspection PyUnresolvedReferences
async def setup_postgres():
    from . import models
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
