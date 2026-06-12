from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship


class TaxMasukanModel(Base):
    __tablename__ = "taxentry"

    faktur_rmy = Column(Integer, primary_key=True, nullable=False)
    kode = Column(String, nullable=False)
    pay_date = Column(String, nullable=False)
    supplier_code = Column(String, nullable=False)
    tgl_faktur = Column(String, nullable=False)
    dpp = Column(String, nullable=False)
    ppn = Column(String, nullable=False)
    no_seri = Column(String, nullable=False)
    tax_date = Column(String, nullable=False)
    npwp = Column(String, nullable=False)
    ppn_con = Column(String, nullable=False)
    release = Column(Boolean, default=True)
    status_ap = Column(Boolean, default=True)
    doc_no = Column(String, nullable=False)
    company_code = Column(String, nullable=False)
    ref_no = Column(String, nullable=False)
    user_create = Column(String, nullable=False)
    date_create = Column(DateTime(timezone=True), server_default=func.now())
    user_modified = Column(String, nullable=False)
    date_modified = Column(DateTime(timezone=True), server_default=func.now())
    supplier_code = Column(String, ForeignKey("supplier.supplier_code"))

    supplier = relationship('SupplierModel', back_populates="tax_masukan")