from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class User(Base):
    name: Mapped[str]
    balance: Mapped[int]