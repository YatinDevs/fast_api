@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup sequence
    await db_startup()
    await cache_startup()
    await background_tasks_start()
    
    yield
    
    # Shutdown sequence (reverse order)
    await background_tasks_stop()
    await cache_shutdown()
    await db_shutdown()