from sqlalchemy.orm import Session
from app.models.employee.mutasi_employee_model import MutasiEmployeeModel
from app.models.employee.master_employee_model import MasterEmployeeModel
from app.schemas.employee.mutasi_employee_schema import MutasiEmployeeBase, CreateMutasiEmployeeBase, CreateMutasiEmployeeResponse

class MutasiEmployeeRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_mutasi_employee_repository(self, skip: int = 0, limit: int = 10):
    result = self.db.query(MutasiEmployeeModel).offset(skip).limit(limit).all()
    return result
  
  def get_master_employee_repository(self, id_employee: int, skip: int = 0, limit: int = 10):
    result = self.db.query(MasterEmployeeModel).where(MasterEmployeeModel.id_employee == id_employee).first()
    return result

  def create_mutasi_employee_repository(self, data: dict) -> MutasiEmployeeModel:
    result = MutasiEmployeeModel(**data)
    self.db.add(result)
    self.db.commit()
    self.db.refresh(result)
    return result
