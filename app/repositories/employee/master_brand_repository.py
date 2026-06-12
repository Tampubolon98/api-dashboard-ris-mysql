from sqlalchemy.orm import Session
from app.models.employee.master_brand_model import MasterBrandModel

class MasterBrandRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_master_brand_repository(self, skip: int = 0, limit: int = 10):
    result = self.db.query(MasterBrandModel).offset(skip).limit(limit).all()
    return result