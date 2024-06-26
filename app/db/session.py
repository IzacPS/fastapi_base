from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

class Base(AsyncAttrs, DeclarativeBase):
    pass

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(autoflush=False, bind=engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with SessionLocal() as session:
        yield session


