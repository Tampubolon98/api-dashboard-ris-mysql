from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MutasiEmployeeBase(BaseModel):
    id_employee: int
    nama: str
    tanggal_masuk: datetime = Field(default_factory=datetime.now)
    tanggal_keluar: datetime = Field(default_factory=datetime.now)
    kategori_karyawan: str
    kode_toko: str
    md_emp: str
    brand_emp: str
    supplier: str
    no_ktp: str
    no_kk: str
    user_create: str
    date_create: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True

class MutasiEmployeeResponse(BaseModel):
    status: bool
    total_data: int
    data: List[MutasiEmployeeBase]

class CreateMutasiEmployeeBase(BaseModel):
    id_employee: int
    brand_emp: str

    class Config:
        from_attributes = True

class CreateMutasiEmployeeResponse(BaseModel):
    status: bool
    message: str
    data: CreateMutasiEmployeeBase