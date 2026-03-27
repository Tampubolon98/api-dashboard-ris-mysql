from fastapi import FastAPI
from app.routers import tax

app = FastAPI()

app.include_router(tax.router)

@app.get("/")
async def root():
  return {
    "message": "API Dashboard RIS"
  }