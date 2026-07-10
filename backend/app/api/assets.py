from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.asset import Asset
from app.schemas.asset import AssetCreate

router = APIRouter(prefix="/assets", tags=["Assets"])


@router.post("/")
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    new_asset = Asset(
        asset_tag=asset.asset_tag,
        serial_number=asset.serial_number,
        asset_type=asset.asset_type,
        brand=asset.brand,
        model=asset.model,
        cpu=asset.cpu,
        ram_gb=asset.ram_gb,
        storage_gb=asset.storage_gb,
        operating_system=asset.operating_system,
        lamp_type=asset.lamp_type,
        status=asset.status,
    )

    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)

    return new_asset