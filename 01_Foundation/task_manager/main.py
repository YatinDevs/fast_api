from sqlalchemy import text 
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import engine
from app.api.v1 import router as api_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
        # Initialize database tables
    from app.core.database import init_db
    await init_db()
    # Startup code
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database connected")
    except Exception as e:
        print("❌ Database connection failed")
        raise e
    
    yield  # App runs here
    
    # Shutdown code (optional)
    await engine.dispose()
    print("🚪 Database connection closed")

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan  # Register the lifespan handler
)

app.include_router(api_router, prefix="/api/v1")
