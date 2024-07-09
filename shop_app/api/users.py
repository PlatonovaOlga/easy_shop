from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.repo import UserRepo
from core.schemas import UserRead, UserCreate
from core.models import db_helper


router = APIRouter(tags=["Users"])


@router.get("", response_model=List[UserRead])
async def get_users(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)]
):
    users_list = await UserRepo.get_all(session=session)
    return users_list


@router.post("", response_model=UserRead)
async def create_user(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
    user: UserCreate
) -> UserRead:
    new_user = await UserRepo.create(
        session=session, 
        user_create=user)
    
    return new_user


@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
    user_id: int
):
    return await UserRepo.get_by_id(session=session, id=user_id)


@router.delete("/{user_id}")
async def delete_user(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)],
        user_id: int
):
    await UserRepo.delete(session=session, id=user_id)