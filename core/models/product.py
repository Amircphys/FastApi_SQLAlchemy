from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

class Product(BaseModel):
    name: Mapped[str]
    descripiton: Mapped[str]
    price: Mapped[float]
    
    