from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MasterBrandBase(BaseModel):
  md: str
  detail_brand: str
  nama_supplier: str
  id_brand_emp: str
  user_create: str
  date_create: datetime = Field(default_factory=datetime.now)
  user_modified: str
  date_modified: datetime = Field(default_factory=datetime.now)

class MasterBrandResponse(BaseModel):
  status: bool
  total_data: int
  data: List[MasterBrandBase]