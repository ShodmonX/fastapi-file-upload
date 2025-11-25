from .upload import router as upload_router

from fastapi import APIRouter

router = APIRouter()
router.include_router(upload_router)