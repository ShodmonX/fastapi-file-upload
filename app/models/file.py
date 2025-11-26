from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.db import Base


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    filename: Mapped[str] = mapped_column(String(255))
    path: Mapped[str] = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)

    processed: Mapped[bool] = mapped_column(Boolean, server_default="false")
    processing_status: Mapped[str] = mapped_column(String(20), server_default="pending")
    thumbnail_path: Mapped[str | None] = mapped_column(String(500), nullable=True)

    uploaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())