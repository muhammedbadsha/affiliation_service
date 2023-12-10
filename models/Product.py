from sqlalchemy import Boolean,Column,String,DateTime,ForeignKey,Float,Integer
from data_base.postgresql import Base
from sqlalchemy.sql import func
from typing import List
from schemas.product import Product
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Product_DB(Base):
    __tablename__ = 'products'
    __allow_unmapped__ = True
    product_id :int = Column(Integer, primary_key=True,autoincrement=True)
    name : str = Column(String)
    affiliate_id :List[UUID] = Column(UUID(as_uuid=True), ForeignKey("affiliated.id"))    
    product_price :float= Column(Float)
    created_at  =  Column(DateTime(timezone=True), server_default=func.now())
    
    affiliate = relationship("Affiliate_DB", back_populates="products")