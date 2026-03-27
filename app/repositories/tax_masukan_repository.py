from sqlalchemy.orm import Session
from app.models.tax_masukan_model import TaxMasukanModel

class TaxMasukanRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_tax_bahan_repository(self, skip: int=0, limit: int=10):
    result = self.db.query(TaxMasukanModel).offset(skip).limit(limit).all()
    return result