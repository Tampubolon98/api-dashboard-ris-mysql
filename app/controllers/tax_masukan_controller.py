from sqlalchemy.orm import Session
from app.repositories.tax_masukan_repository import TaxMasukanRepository

class TaxMasukanController:
  def __init__(self, db: Session):
    self.db = db

  def get_tax_bahan_controller(self, skip: int=0, limit: int=10):
    repo = TaxMasukanRepository(db=self.db)
    data = repo.get_tax_bahan_repository(skip=skip, limit=limit)

    return {
      "status": True,
      "total_data": len(data),
      "data": data
    }