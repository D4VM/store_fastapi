from odmantic import Model, Field


class ProductModel(Model):
    category: str = Field(default='All')
    title: str
    description: str
    price: float = Field(default=0, ge=0)
    stock: int = Field(default=0, ge=0)
    published: bool = Field(default=False)
