from fastapi import FastAPI
from src.router import product

app = FastAPI()
app.include_router(product.router)

@app.get("/",tags=["Home"])
async def dashboard():
    return "Hello World!"