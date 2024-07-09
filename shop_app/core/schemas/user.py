from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    balance: int

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int