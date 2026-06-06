from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[int] = None
    title: str
    price: float
    description: str
    category: str
    image: Optional[str] = "https://via.placeholder.com/300"