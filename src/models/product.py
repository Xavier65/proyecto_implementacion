from pydantic import BaseModel

class Product(BaseModel):
    codigo:str
    description:str
    quantity:float
    price:float
