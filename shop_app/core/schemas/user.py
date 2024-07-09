from pydantic import BaseModel, ConfigDict

class UserBaseSchema(BaseModel):
    name: str
    balance: int

class UserCreateSchema(UserBaseSchema):
    pass

class UserReadSchema(UserBaseSchema):
    id: int