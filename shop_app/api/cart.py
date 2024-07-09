from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.repo import CartRepo
from core.schemas import CartRead, CartCreate
from core.models import db_helper


router = APIRouter(tags=["Carts"])


@router.get("", response_model=List[CartRead])
async def get_Carts(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)]
):
    carts_list = await CartRepo.get_all(session=session)
    return carts_list


@router.post("", response_model=CartRead)
async def create_cart(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
    cart: CartCreate
) -> CartRead:
    new_cart = await CartRepo.create(
        session=session, 
        cart_create=cart)
    
    return new_cart


@router.get("/{cart_id}", response_model=CartRead)
async def get_cart_by_id(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
    cart_id: int
):
    return await CartRepo.get_by_id(session=session, id=cart_id)


@router.delete("/{cart_id}")
async def delete_cart(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
        cart_id: int
):
    await CartRepo.delete(session=session, id=cart_id)