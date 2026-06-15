from sqlalchemy.orm import Session
from app.models.tax.tax_masukan_model import TaxMasukanModel
from app.models.supplier_model import SupplierModel

class TaxMasukanRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_tax_bahan_repository(self, skip: int = 0, limit: int = 10):
    result = (
        self.db.query(TaxMasukanModel, SupplierModel)
        .join(
            SupplierModel,
            TaxMasukanModel.supplier_code == SupplierModel.supplier_code
        )
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result