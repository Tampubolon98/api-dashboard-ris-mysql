import pandas as pd
from io import BytesIO
from app.repositories.employee.master_brand_repository import MasterBrandRepository
from app.models.employee.master_brand_model import MasterBrandModel
from datetime import datetime
import traceback

class MasterBrandService:
    def __init__(self, db):
        self.db = db

    def create_brands(self, file):
        try:
            if not file.filename.endswith((".xlsx", ".xls")):
                return {
                    "status": False,
                    "message": "File harus excel"
                }

            content = file.file.read()

            df = pd.read_excel(
                BytesIO(content),
                dtype=str
            )

            column_mapping = {
                "id_brand_emp": "ID Brand Employee",
                "detail_brand": "Detail Brand",
                "nama_supplier": "Nama Supplier"
            }

            missing_columns = []

            for excel_column in column_mapping.values():
                if excel_column not in df.columns:
                    missing_columns.append(excel_column)

            if missing_columns:
                return {
                    "status": False,
                    "message": f"Kolom {', '.join(missing_columns)} tidak ditemukan"
                }

            data = []
            for _, row in df.iterrows():
                data.append(
                    MasterBrandModel(
                        id_brand_emp=row[column_mapping["id_brand_emp"]],
                        detail_brand=row[column_mapping["detail_brand"]],
                        nama_supplier=row[column_mapping["nama_supplier"]],
                        user_create="SYSTEM"
                    )
                )

            repo = MasterBrandRepository(self.db)
            repo.create_brand(data)

            return {
                "status": True,
                "message": f"Data berhasil ditambahkan"
            }

        except Exception as e:
            self.db.rollback()
            print(traceback.format_exc())

            return {
                "status": False,
                "message": str(e)
            }