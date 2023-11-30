from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.settings import settings

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}".format(
    user=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
    db=settings.postgres_db,
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()
