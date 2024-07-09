from pydantic import BaseModel, ConfigDict

class ProductBaseSchema(BaseModel):
    #model_config = ConfigDict(from_attributes=True)
    name: str
    price: int

class ProductCreateSchema(ProductBaseSchema):
    pass

class ProductReadSchema(ProductBaseSchema):
    # model_config = ConfigDict(
    #     from_attributes=True
    # )
    id: int