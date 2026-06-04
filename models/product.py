from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: Optional[str] = "https://via.placeholder.com/300"


class UpdatedProduct(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: Optional[str] = "https://via.placeholder.com/300"