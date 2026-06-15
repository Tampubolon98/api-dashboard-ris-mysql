from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.employee.master_employee_schema import MasterEmployeeResponse
from app.controllers.employee.master_employee_controller import MasterEmployeeController
from app.schemas.employee.master_brand_schema import MasterBrandResponse
from app.controllers.employee.master_brand_controller import MasterBrandController

router = APIRouter()

@router.get("/master-employee/get", response_model=MasterEmployeeResponse, tags=["Master Employee"])
async def get_master_employee(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0
):
    query = MasterEmployeeController(db)
    result = query.get_master_employee_controller(skip=skip, limit=limit)
    return result

@router.get("/master-brand/get", response_model=MasterBrandResponse, tags=["Master Brand"])
async def get_master_brand(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0
):
    query = MasterBrandController(db)
    result = query.get_master_brand_controller(skip=skip, limit=limit)
    return result