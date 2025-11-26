from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def create_file(db: AsyncSession, hash: str, filename: str | None, path: str, user_id: int):
    stm = text("""
        INSERT INTO files (hash, filename, path, user_id)
        VALUES (:hash, :filename, :path, :user_id)
        RETURNING *
    """)
    result = await db.execute(statement=stm, params={
        "hash": hash,
        "filename": filename,
        "path": path,
        "user_id": user_id
    })
    await db.commit()
    return result.mappings().first()

async def get_file(db: AsyncSession, file_hash: str):
    stm = text("""
        SELECT *
        FROM files
        WHERE hash = :hash     
    """)

    result = await db.execute(statement=stm, params={
        "hash": file_hash
    })
    return result.mappings().first()

async def update_file_status(db: AsyncSession, id: int, processing_status: str, processed: bool):
    stm = text("""
        UPDATE files
        SET processing_status = :processing_status, processed = :processed
        WHERE id = :id 
        RETURNING *
    """)

    result = await db.execute(statement=stm, params={
        "id": id,
        "processing_status": processing_status,
        "processed": processed
    })
    await db.commit()
    return result.mappings().first()

async def update_file_thumbnail(db: AsyncSession, id: int, thumbnail_path: str):
    stm = text("""
        UPDATE files
        SET thumbnail_path = :thumbnail_path
        WHERE id = :id 
        RETURNING *
    """)

    result = await db.execute(statement=stm, params={
        "id": id,
        "thumbnail_path": thumbnail_path
    })
    await db.commit()
    return result.mappings().first()
