from sqlalchemy.orm import Session
from app.repositories.employee.master_employee_repository import MasterEmployeeRepository

class MasterEmployeeController:
  def __init__(self, db: Session):
    self.db = db

  def get_master_employee_controller(self, skip: int=0, limit: int=10):
    repo = MasterEmployeeRepository(db=self.db)
    data = repo.get_master_employee_repository(skip=skip, limit=limit)

    return {
      "status": True,
      "total_data": len(data),
      "data": data
    }