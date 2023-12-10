from sqlalchemy import Boolean,Column,String,DateTime,ForeignKey,Float,Integer
from data_base.postgresql import Base
from sqlalchemy.sql import func
from typing import List
from schemas.product import Product
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship



class Affiliate_DB(Base):
    __tablename__ = 'affiliated'
    id :str = Column(String, primary_key=True, default=str(uuid.uuid1()), index=True)
    name  :str = Column(String)
    commission_rate :float = Column(Float)
    commission:float = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    products = relationship("Product_DB", back_populates="affiliate")
    


