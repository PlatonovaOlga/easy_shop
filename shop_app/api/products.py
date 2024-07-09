from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.repo import ProductRepo
from core.schemas import ProductRead, ProductCreate
from core.models import db_helper


router = APIRouter(tags=["Products"])


@router.get("", response_model=List[ProductRead])
async def get_products(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)]
):
    products_list = await ProductRepo.get_all(session=session)
    return products_list


@router.post("", response_model=ProductRead)
async def create_product(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
    product: ProductCreate
) -> ProductRead:
    new_product = await ProductRepo.create(
        session=session, 
        product_create=product)
    
    return new_product


@router.get("/{product_id}", response_model=ProductRead)
async def get_product_by_id(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
    product_id: int
):
    return await ProductRepo.get_by_id(session=session, id=product_id)


@router.delete("/{product_id}")
async def delete_product(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
        product_id: int
):
    await ProductRepo.delete(session=session, id=product_id)