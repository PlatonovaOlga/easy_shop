from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from core.schemas import ProductCreateSchema


class ProductRepo:
    @classmethod
    async def get_by_id(
            cls,
            session: AsyncSession,
            id: int
    ) -> Product:
        return await session.get(Product, id)


    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[Product]:
        stmt = select(Product).order_by(Product.id)
        result = await session.scalars(stmt)
        return result.all()


    @classmethod
    async def create(
        cls,
        session: AsyncSession,
        product_create: ProductCreateSchema
    ) -> Product:
        product = Product(**product_create.model_dump())
        session.add(product)
        await session.commit()
        #await session.refresh(product)
        return product

    @classmethod
    async def delete(cls, session: AsyncSession, id: int) -> None:
        product = await session.get(Product, id)
        await session.delete(product)
        await session.commit()
    