### Code Explanation

```python
from fastapi import FastAPI
from app.core.database import engine
from app.api.v1 import router as api_router
```

- **Lines 1-3**: Imports the necessary components
  - `FastAPI` class to create your application instance
  - `engine` from your database configuration (SQLAlchemy async engine)
  - Versioned API router from `app/api/v1`

```python
app = FastAPI(title="Task Manager API")
```

- **Line 5**: Creates the FastAPI application instance with a title

```python
@app.on_event("startup")
async def startup_db_check():
```

- **Lines 7-8**: Defines a startup event handler that runs when the application starts

```python
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database connection established")
```

- **Lines 9-12**: Tests database connectivity by executing a simple SQL query
  - `engine.begin()` creates a new connection
  - `text("SELECT 1")` is a simple SQL statement
  - Prints success message if connection works

```python
    except Exception as e:
        print("❌ Database connection failed")
        raise e
```

- **Lines 13-15**: Handles connection failures by printing an error and raising the exception

```python
app.include_router(api_router, prefix="/api/v1")
```

- **Line 17**: Mounts your API router with "/api/v1" prefix for all routes

### Adding a Test Route

Add this to your `app/api/v1/__init__.py` (or wherever your router is defined):

```python
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/test", response_class=HTMLResponse)
async def test_browser():
    return """
    <html>
        <head>
            <title>Test Page</title>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 50px; }
                .success { color: green; font-size: 24px; }
            </style>
        </head>
        <body>
            <h1>FastAPI Test Route</h1>
            <p class="success">✓ API is working</p>
            <p>Database status will appear in your console on startup</p>
        </body>
    </html>
    """
```

### How to Test:

1. Run your FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

2. Open in browser:

   ```
   http://localhost:8000/api/v1/test
   ```

3. You should see:
   - A green checkmark confirming the API works
   - In your terminal, either:
     - ✅ Database connection established (success)
     - ❌ Database connection failed (error will show details)

### Key Points:

- The startup check runs automatically when you launch the app
- The test route gives you visual confirmation in browser
- Both routes are async-enabled for proper async database handling
- The HTML response demonstrates FastAPI's flexible response handling

# Create virtual environment

    bash

            python -m venv venv
            source venv/bin/activate # Linux/Mac

# venv\Scripts\activate # Windows

# Install core packages

    pip install fastapi uvicorn sqlalchemy asyncpg pydantic

# Create a Folder Structure

mkdir task_manager, task_manager\app, task_manager\app\core, task_manager\app\models, task_manager\app\schemas, task_manager\app\crud, task_manager\app\api, task_manager\app\api\v1, task_manager\app\dependencies, task_manager\app\utils, task_manager\alembic, task_manager\tests, task_manager\requirements

# Create Database file

make database.py file in app -> core -> database.py

## Setup for PostgresSQL

        from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.pool import NullPool

        DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/taskdb"

        # Recommended for production:
        engine = create_async_engine(
            DATABASE_URL,
            poolclass=NullPool,  # Disable connection pooling for ASGI
            echo=True  # Log SQL queries in dev
        )

        AsyncSessionLocal = sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False
        )

        async def get_db():
            async with AsyncSessionLocal() as session:
                yield session

## Setup for MySQl

- to install we need to activate enviorment :

        .\venv\Scripts\activate

        deactivate

- Only create one virtual environment per project (in your case, inside task_manager)

- Always navigate to your project root (task_manager) before activating

- install from project root directory :

  pip install fastapi uvicorn sqlalchemy asyncpg python-dotenv
#   f a s t _ a p i  
 