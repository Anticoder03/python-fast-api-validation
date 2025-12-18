from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="FastAPI Validation Project",
    description="Simple CRUD with proper validation",
    version="1.0.0"
)

app.include_router(router)
