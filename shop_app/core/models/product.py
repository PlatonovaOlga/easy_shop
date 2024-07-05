from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class Product(Base):
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]