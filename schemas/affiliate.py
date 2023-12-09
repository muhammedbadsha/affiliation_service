from pydantic import BaseModel


class Affiliate(BaseModel):
    Affiliate_id : str
    name : str
    product_id : int
    commition_rate : float
