from odmantic import ObjectId
from pydantic import BaseModel, Field


class SProduct(BaseModel):
    category: str = Field(default='All', examples=['Mobile Phones'])
    title: str = Field(default='Product Title', examples=['iPhone 15 PRO MAX ULTRA'])
    description: str = Field(default="Description", examples=['Bigger better Ultraaaa'])
    price: float = Field(default=0, ge=0, examples=[7999.00])
    stock: int = Field(default=0, ge=0, examples=[10])
    published: bool = Field(default=False, examples=[True])