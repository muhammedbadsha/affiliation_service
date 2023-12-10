from pydantic import BaseModel,UUID1
import uuid
# from schemas.affiliate import Affiliate
from typing import List


class Product(BaseModel):
    name : str

    product_price:float
    affiliate_id: List[UUID1]

    class Config:
        orm_mode = True