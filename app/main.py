from fastapi import FastAPI

from app import settings
from app.routers import router


app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    openapi_url="/openapi.json" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None
)

app.include_router(router)

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}