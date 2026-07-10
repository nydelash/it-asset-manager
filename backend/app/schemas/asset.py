from pydantic import BaseModel
from typing import Optional


class AssetCreate(BaseModel):
    asset_tag: str
    serial_number: str

    asset_type: str
    brand: str
    model: str

    cpu: Optional[str] = None
    ram_gb: Optional[int] = None
    storage_gb: Optional[int] = None
    operating_system: Optional[str] = None

    lamp_type: Optional[str] = None

    status: str = "Disponible"