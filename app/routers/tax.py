from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.tax.tax_masukan_schema import TaxMasukanResponse
from app.controllers.tax.tax_masukan_controller import TaxMasukanController

router = APIRouter()

@router.get("/tax-bahan/get", response_model=TaxMasukanResponse, tags=["Tax Bahan"])
async def get_tax_bahan(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0
):
    query = TaxMasukanController(db)
    result = query.get_tax_bahan_controller(skip=skip, limit=limit)
    return result