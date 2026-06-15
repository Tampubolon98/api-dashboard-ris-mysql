from sqlalchemy.orm import Session
from app.models.employee.master_employee_model import MasterEmployeeModel

class MasterEmployeeRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_master_employee_repository(self, skip: int = 0, limit: int = 10):
    result = self.db.query(MasterEmployeeModel).offset(skip).limit(limit).all()
    return result