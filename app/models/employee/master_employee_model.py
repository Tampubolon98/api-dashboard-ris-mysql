from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class MasterEmployeeModel(Base):
  __tablename__ = "master_employee_spg"

  nama = Column(String, nullable=False)
  alamat = Column(String, nullable=False)
  tanggal_lahir = Column(DateTime(timezone=True), server_default=func.now())
  kota = Column(String, nullable=False)
  kode_toko = Column(String, nullable=False)
  no_handphone = Column(String, nullable=False)
  tanggal_masuk = Column(DateTime(timezone=True), server_default=func.now())
  no_kk = Column(String, nullable=False)
  no_ktp = Column(String, nullable=False)
  data_pola = Column(String, nullable=False)
  id_employee = Column(Integer, primary_key=True, nullable=False)
  jenis_kelamin = Column(String, nullable=False)
  status = Column(String, nullable=False)
  supplier = Column(String, nullable=False)
  alamat_rumah = Column(String, nullable=False)
  user_create = Column(String, nullable=False)
  date_create = Column(DateTime(timezone=True), server_default=func.now())
  user_updated = Column(String, nullable=False)
  date_updated = Column(DateTime(timezone=True), server_default=func.now())
  keterangan = Column(String, nullable=False)
  tanggal_keluar = Column(DateTime(timezone=True), server_default=func.now())
  status_aktif = Column(String, nullable=False)
  user_terminate = Column(String, nullable=False)
  date_terminate = Column(DateTime(timezone=True), server_default=func.now())
  image_employee = Column(String, nullable=False)
  kategori_karyawan = Column(String, nullable=False)
  md_emp = Column(String, nullable=False)
  brand_emp = Column(String, nullable=False)
  tanggal_selesai = Column(DateTime(timezone=True), server_default=func.now())

