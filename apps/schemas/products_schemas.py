from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict

class ProductCreateSchema(BaseModel):
    name: str = Field(min_length=4, max_length=50)
    qtt: int = Field(gt=0)
    expiration_date: date
    price: float = Field(gt=0.0)
    img: str | None = None

class ProductUpdateSchema(BaseModel):
    qtt: int | None = Field(None, ge=0)
    price: float | None = Field(None, gt=0.0)
    img: str | None = None

class ProductResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_product: int
    name: str
    qtt: int
    expiration_date: date
    price: float
    img: str | None = None
    created_at: datetime