from typing import Optional

from pydantic import BaseModel


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
