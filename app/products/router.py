from fastapi import APIRouter
from app.products.models import ProductModel
from app.products.services import ProductService
from app.products.schemas import SProduct

router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.post('/add', response_model=SProduct)
def add_product(product: SProduct):
    pr = ProductService.add_one_product(product)
    return pr