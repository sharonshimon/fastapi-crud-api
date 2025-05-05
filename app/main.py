from fastapi import FastAPI

from .db import Base, engine
from .routers.users import router as users_router
from .routers.partners import router as partners_router


# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI CRUD",
    version="1.0.0",
    description="v1 endpoints for User and Partner CRUD",
)

app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
)

app.include_router(
    partners_router,
    prefix="/api/v1",
    tags=["partners"],
)