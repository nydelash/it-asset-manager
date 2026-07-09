from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    asset_tag: Mapped[str] = mapped_column(String(50), unique=True)
    serial_number: Mapped[str] = mapped_column(String(100), unique=True)

    asset_type: Mapped[str] = mapped_column(String(50))
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(100))

    cpu: Mapped[str | None] = mapped_column(String(100), nullable=True)
    ram_gb: Mapped[int | None] = mapped_column(nullable=True)
    storage_gb: Mapped[int | None] = mapped_column(nullable=True)
    operating_system: Mapped[str | None] = mapped_column(String(100), nullable=True)

    lamp_type: Mapped[str | None] = mapped_column(String(100), nullable=True)

    status: Mapped[str] = mapped_column(String(50), default="Disponible")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )