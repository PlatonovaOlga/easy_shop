from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    #model_config = ConfigDict(from_attributes=True)
    name: str
    price: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    # model_config = ConfigDict(
    #     from_attributes=True
    # )
    id: int