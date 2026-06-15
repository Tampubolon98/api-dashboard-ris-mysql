from fastapi import FastAPI
from app.routers import tax, employee

app = FastAPI()

app.include_router(tax.router)
app.include_router(employee.router)

@app.get("/")
async def root():
  return {
    "message": "API Dashboard RIS"
  }