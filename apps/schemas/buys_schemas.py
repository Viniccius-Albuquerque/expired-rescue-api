from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class BuyCreateSchema(BaseModel):
    id_product: int = Field(gt = 0, description = "ID do produto a ser comprado")
    qtt: int = Field(gt = 0, description = "Quantidade do produto a ser comprado")


class BuyUpdateSchema(BaseModel):
    qtt: int = Field(gt = 0, description = "Quantidade do produto a ser comprado")


class BuyResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id_buy: int
    id_user: int
    id_product: int
    qtt: int
    price_at_buy: float
    status: Literal ['processing', 'completed', 'canceled']
    time: datetime