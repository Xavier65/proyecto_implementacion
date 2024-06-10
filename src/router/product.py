from fastapi import APIRouter
from src.models import Product
from src.manager import Manager

router = APIRouter(tags=["Products"])
PRODUCT:str = "Product"

@router.get("/product/{product_id}")
async def find_product(product_id:int):
    return f"Find Product -> {product_id}"

@router.post("/product/")
async def new_product(product: Product):
    Manager.insert(PRODUCT,product)
    return product

@router.put("/product/{product_id}")
async def update_product(product: Product, product_id:int):
    return f"{product.model_dump()} -> {product_id}"

@router.delete("/product/{product_id}")
async def delete_product(product_id:int):
    return f"Delete {product_id}"