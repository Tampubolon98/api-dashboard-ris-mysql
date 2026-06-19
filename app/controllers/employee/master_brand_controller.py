from sqlalchemy.orm import Session
from app.repositories.employee.master_brand_repository import MasterBrandRepository
from app.services.employee.master_brand_service import MasterBrandService

class MasterBrandController:
  def __init__(self, db: Session):
    self.db = db

  def get_master_brand_controller(self, skip: int=0, limit: int=10):
    repo = MasterBrandRepository(db=self.db)
    data = repo.get_master_brand_repository(skip=skip, limit=limit)

    return {
      "status": True,
      "total_data": len(data),
      "data": data
    }
  
  def create_master_brand_controller(self, data):
    repo = MasterBrandRepository(db=self.db)
    result = repo.create_master_brand_repository(data=data)

    return {
      "status": True,
      "message": "Data berhasil ditambahkan",
      "data": result
    }
  
  def create_master_brand_controller(self, payload):
    repo = MasterBrandService(db=self.db)
    result = repo.create_brands(file=payload)
    return result