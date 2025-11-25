from fastapi import APIRouter, UploadFile, File, Depends, status, HTTPException, Path
from fastapi.responses import FileResponse

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from pathlib import Path
import uuid
import os

from app.db import get_db
from app.core import get_bytes_hash
from app.crud import get_file, create_file


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True, parents=True)

router = APIRouter(
    prefix="/upload",
    tags=["File Upload"]
)

@router.post("/")
async def upload_file(
    file: Annotated[UploadFile, File()],
    db: Annotated[AsyncSession, Depends(get_db)],
    user: int = 1,
) -> dict[str, str]:

    if file.content_type and not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You can only upload image files"
        )

    contents = await file.read()

    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size must be less than 5 MB"
        )

    file_hash = get_bytes_hash(contents)

    file_db = await get_file(db, file_hash)

    if file_db:
        return {
            "hash": file_db.hash,
            "url": f"http://localhost:8080/upload/files/{file_db.hash}/",
            "filename": file_db.filename or ""
        }

    safe_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = UPLOAD_DIR / safe_filename

    with open(file_path, "wb") as f:
        f.write(contents)

    await create_file(db, file_hash, file.filename, str(file_path), user)

    return {
        "hash": file_hash,
        "url": f"http://localhost:8080/upload/files/{file_hash}/",
        "filename": file.filename if file.filename else ""
    }

@router.get("/files/{file_hash}/")
async def read_file(
    file_hash: Annotated[str, Path()],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    file_path = await get_file(db, file_hash)
    if not file_path:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found"
        )
    if "path" not in file_path:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found"
        )
    return FileResponse(file_path['path'])
    