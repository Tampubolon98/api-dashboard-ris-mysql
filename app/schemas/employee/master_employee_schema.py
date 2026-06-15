from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MasterEmployeeBase(BaseModel):
    nama: str
    alamat: str
    tanggal_lahir: datetime = Field(default_factory=datetime.now)
    kota: str
    kode_toko: str
    no_handphone: str
    tanggal_masuk: datetime = Field(default_factory=datetime.now)
    no_kk: str
    no_ktp: str
    data_pola: str
    id_employee: int
    jenis_kelamin: str
    status: str
    supplier: str
    alamat_rumah: str
    user_create: str
    date_create: datetime = Field(default_factory=datetime.now)
    user_updated: str
    date_updated: datetime = Field(default_factory=datetime.now)
    keterangan: str
    tanggal_keluar: datetime = Field(default_factory=datetime.now)
    status_aktif: str
    user_terminate: str
    date_terminate: datetime = Field(default_factory=datetime.now)
    image_employee: str
    kategori_karyawan: str
    md_emp: str
    brand_emp: str
    tanggal_selesai: datetime = Field(default_factory=datetime.now)