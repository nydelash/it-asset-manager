
from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.asset import Asset
from app.api.assets import router as asset_router



Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(asset_router)

@app.get("/")
def root():
    return {"message": "IT Asset Manager API"}