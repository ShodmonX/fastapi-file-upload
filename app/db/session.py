from sqlalchemy.ext.asyncio import AsyncSession

from typing import AsyncGenerator

from .base import LocalSession


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with LocalSession() as session:
        yield session