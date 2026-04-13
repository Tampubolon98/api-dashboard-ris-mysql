from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TaxMasukanBase(BaseModel):
    faktur_rmy: str
    kode: str
    pay_date: datetime = Field(default_factory=datetime.now)
    supplier_code: str
    tgl_faktur: datetime = Field(default_factory=datetime.now)
    dpp: Optional[float]
    ppn: Optional[float]
    no_seri: str
    tax_date: datetime = Field(default_factory=datetime.now)
    npwp: str
    ppn_con: Optional[float]
    release: Optional[int]
    status_ap: Optional[int]
    doc_no: Optional[str]
    company_code: Optional[str]
    ref_no: Optional[str]
    user_create: str
    date_create: datetime = Field(default_factory=datetime.now)
    user_modified: str
    date_modified: Optional[datetime]

    class Config:
        from_attributes = True

class TaxMasukanResponse(BaseModel):
    status: bool
    total_data: int
    data: List[TaxMasukanBase]