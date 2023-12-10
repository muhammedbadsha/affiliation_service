from pydantic import BaseModel
from typing import List
from schemas.product import Product
class Affiliate(BaseModel):
    # id : str
    name : str
    commition_rate : float
    commission: float
   

    class Config:
        orm_mode = True
