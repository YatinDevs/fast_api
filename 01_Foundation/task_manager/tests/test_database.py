@pytest.mark.asyncio
async def test_database_connection():
    from app.core.database import engine
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar() == 1