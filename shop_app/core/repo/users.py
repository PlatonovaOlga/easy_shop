from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from core.schemas.user import UserCreate


class UserRepo:
    @classmethod
    async def get_by_id(
            cls,
            session: AsyncSession,
            id: int
    ) -> User:
        return await session.get(User, id)


    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[User]:
        stmt = select(User).order_by(User.id)
        result = await session.scalars(stmt)
        return result.all()


    @classmethod
    async def create(
        cls,
        session: AsyncSession,
        user_create: UserCreate
    ) -> User:
        user = User(**user_create.model_dump())
        session.add(user)
        await session.commit()
        #await session.refresh(user)
        return user

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> None:
        user = await session.get(User, id)
        await session.delete(user)
        await session.commit()
    