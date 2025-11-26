import logging
from pathlib import Path
from PIL import Image
import asyncio

logger = logging.getLogger(__name__)

async def process_file(file_path_: str, file_id: int, db):
    from app.crud import update_file_status
    file_path = Path(file_path_)
    
    try:
        if file_path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
            await _create_thumbnail(file_path, file_id, db)
        
        await update_file_status(db, file_id, "success", processed=True)
        logger.info(f"File {file_id} processed successfully")
    
    except Exception as e:
        logger.error(f"Background processing failed for file {file_id}: {e}")
        await update_file_status(db, file_id, "failed", processed=True)

async def _create_thumbnail(file_path: Path, file_id: int, db):
    thumb_dir = file_path.parent / "thumbs"
    thumb_dir.mkdir(exist_ok=True)
    thumb_path = thumb_dir / f"thumb_200x200_{file_path.name}"
    
    size = (200, 200)
    with Image.open(file_path) as img:
        img.thumbnail(size)
        img.save(thumb_path, optimize=True, quality=85)
    
    from app.crud import update_file_thumbnail
    await update_file_thumbnail(db, file_id, str(thumb_path))