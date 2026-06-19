from sqlalchemy.orm import Session
from app.models.employee.master_brand_model import MasterBrandModel
from app.schemas.employee.master_brand_schema import MasterBrandBase, CreateMasterBrandBase

class MasterBrandRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_master_brand_repository(self, skip: int = 0, limit: int = 10):
    result = self.db.query(MasterBrandModel).offset(skip).limit(limit).all()
    return result
  
  def create_master_brand_repository(self, data: CreateMasterBrandBase) -> MasterBrandModel:
    result = MasterBrandModel(**data.model_dump())
    self.db.add(result)
    self.db.commit()
    self.db.refresh(result)
    return result
  
  def create_brand(self, data: list[MasterBrandModel]):
    self.db.add_all(data)
    self.db.commit()
    return data