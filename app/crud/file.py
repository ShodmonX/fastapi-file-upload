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