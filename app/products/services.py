from fastapi import HTTPException, status

from app.database import engine
from app.products.models import ProductModel
from app.products.schemas import SProduct


class ProductService:

    @classmethod
    def add_one_product(cls, product: SProduct):
        product_dict = product.dict()
        product_data = ProductModel(**product_dict)
        data = engine.save(product_data)
        return data
