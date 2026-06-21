from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class MutasiEmployeeModel(Base):
  __tablename__ = "mutasi_emp"

  id_employee = Column(Integer, ForeignKey("master_employee_spg.id_employee"), primary_key=True, nullable=False)
  nama = Column(String, nullable=False)
  tanggal_masuk = Column(DateTime(timezone=True), server_default=func.now())
  tanggal_keluar = Column(DateTime(timezone=True), server_default=func.now())
  kategori_karyawan = Column(String, nullable=False)
  kode_toko = Column(String, nullable=False)
  md_emp = Column(String, nullable=False)
  brand_emp = Column(String, nullable=False)
  supplier = Column(String, nullable=False)
  no_ktp = Column(String, nullable=False)
  no_kk = Column(String, nullable=False)
  user_create = Column(String, nullable=False)
  date_create = Column(DateTime(timezone=True), server_default=func.now())
  nama_toko = Column(String, nullable=False)
  user_updated = Column(String, nullable=False)
  date_updated = Column(DateTime(timezone=True), server_default=func.now())

  master_employee = relationship("MasterEmployeeModel", back_populates="mutasi")