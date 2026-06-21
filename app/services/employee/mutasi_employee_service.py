from app.repositories.employee.mutasi_employee_repository import MutasiEmployeeRepository
from app.models.employee.mutasi_employee_model import MutasiEmployeeModel
from datetime import datetime
from sqlalchemy import desc

class MutasiEmployeeService:
  def __init__(self, db):
    self.db = db
  
  def create_mutasi_employee_service(self, data):
    repo = MutasiEmployeeRepository(db=self.db)
    data_employee = repo.get_master_employee_repository(data.id_employee)

    if not data_employee:
      return {
        "status": False,
        "message": "ID Employee tidak ditemukan"
      }
    
    now = datetime.now()
    month = now.strftime("%m")
    year = now.strftime("%y")

    prefix = f"RHO{month}{year}"

    last_data = (
        self.db.query(MutasiEmployeeModel)
        .filter(MutasiEmployeeModel.md_emp.like(f"{prefix}%"))
        .order_by(desc(MutasiEmployeeModel.md_emp))
        .first()
    )

    if last_data:
        last_number = int(last_data.md_emp[-3:])
        running_number = last_number + 1
    else:
        running_number = 1

    md_emp = f"{prefix}{running_number:03d}"
    
    new_data = {
      "id_employee": data.id_employee,
      "nama": data_employee.nama,
      "tanggal_masuk": data_employee.tanggal_masuk,
      "tanggal_keluar": data_employee.tanggal_keluar,
      "kategori_karyawan": data_employee.kategori_karyawan,
      "kode_toko": data_employee.kode_toko,
      "md_emp": md_emp,
      "brand_emp": data.brand_emp,
      "supplier": data_employee.supplier,
      "no_ktp": data_employee.no_ktp,
      "no_kk": data_employee.no_kk,
      "user_create": "SYSTEM",
      "date_create": datetime.now(),
    }
    
    result = repo.create_mutasi_employee_repository(data=new_data)

    return {
      "status": True,
      "message": "Data berhasil ditambahkan",
      "data": result
    }