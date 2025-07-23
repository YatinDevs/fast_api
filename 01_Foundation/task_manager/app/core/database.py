from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from .config import settings
from app.models.base import Base  # Import Base

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/taskdb"

# Recommended for production:
engine = create_async_engine(
    settings.DATABASE_URL,
    poolclass=NullPool,  # Disable connection pooling for ASGI
    echo=True  # Log SQL queries in dev
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session