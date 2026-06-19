from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class MasterBrandModel(Base):
  __tablename__ = "master_brand_emp"

  md = Column(String, nullable=False)
  detail_brand = Column(String, nullable=False)
  nama_supplier = Column(String, nullable=False)
  id_brand_emp = Column(String, primary_key=True, nullable=False)
  user_create = Column(String, nullable=False)
  date_create = Column(DateTime(timezone=True), server_default=func.now())
  user_modified = Column(String, nullable=False)
  date_modified = Column(DateTime(timezone=True), server_default=func.now())