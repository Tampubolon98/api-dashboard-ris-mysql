from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.employee.master_employee_schema import MasterEmployeeBase, MasterEmployeeResponse, CreateMasterEmployeeBase, CreateMasterEmployeeResponse
from app.controllers.employee.master_employee_controller import MasterEmployeeController
from app.schemas.employee.master_brand_schema import MasterBrandResponse, CreateMasterBrandBase, CreateMasterBrandResponse
from app.controllers.employee.master_brand_controller import MasterBrandController
from app.controllers.employee.mutasi_employee_controller import MutasiEmployeeController
from app.schemas.employee.mutasi_employee_schema import MutasiEmployeeResponse, CreateMutasiEmployeeBase,CreateMutasiEmployeeResponse

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

@router.post("/master-employee/create", response_model=CreateMasterEmployeeResponse, tags=["Master Employee"])
async def create_master_employee(
    data: CreateMasterEmployeeBase,
    db: Session = Depends(get_db)
):
    query = MasterEmployeeController(db)
    result = query.create_master_employee_controller(data=data)
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

@router.post("/master-brand/create", response_model=CreateMasterBrandResponse, tags=["Master Brand"])
async def create_master_brand(
    data: CreateMasterBrandBase,
    db: Session = Depends(get_db)
):
    query = MasterBrandController(db)
    result = query.create_master_brand_controller(data=data)
    return result

@router.post("/master-brand", tags=["Master Brand"])
async def master_brand(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    controller = MasterBrandController(db)
    return controller.create_master_brand_controller(payload=file)

@router.get("/mutasi_employee/get", response_model=MutasiEmployeeResponse, tags=["Mutasi Employee"])
async def get_mutasi_employee(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0
):
    query = MutasiEmployeeController(db)
    result = query.get_mutasi_employee_controller(skip=skip, limit=limit)
    return result

@router.post("/mutasi_employee/create", response_model=CreateMutasiEmployeeResponse, tags=["Mutasi Employee"])
async def create_mutasi_employee(
    data: CreateMutasiEmployeeBase,
    db: Session = Depends(get_db)
):
    query = MutasiEmployeeController(db)
    result = query.create_mutasi_employee_controller(data=data)
    return result
