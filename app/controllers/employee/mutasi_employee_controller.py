from sqlalchemy.orm import Session
from app.repositories.employee.mutasi_employee_repository import MutasiEmployeeRepository
from app.services.employee.mutasi_employee_service import MutasiEmployeeService

class MutasiEmployeeController:
  def __init__(self, db: Session):
    self.db = db

  def get_mutasi_employee_controller(self, skip: int=0, limit: int=10):
    repo = MutasiEmployeeRepository(db=self.db)
    data = repo.get_mutasi_employee_repository(skip=skip, limit=limit)

    return {
      "status": True,
      "total_data": len(data),
      "data": data
    }
  
  def create_mutasi_employee_controller(self, data):
    service = MutasiEmployeeService(db=self.db)
    result = service.create_mutasi_employee_service(data=data)

    return result