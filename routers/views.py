from fastapi import APIRouter, Depends, HTTPException, status
from data_base.postgresql import Base, engine_psql, get_psql_db
from sqlalchemy.orm import Session
from schemas.affiliate import Affiliate
from schemas.product import Product
from models.affiliate import Affiliate_DB
from models.Product import Product_DB
from sqlalchemy import text,or_
from typing import Generator
import uuid 


from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine_psql)
routers = APIRouter()


@routers.get("/")
def get_another_value():
    return "valuesadfmksdf"


@routers.post("/create_affiliate")
async def create_affiliate(affiliate: Affiliate, db: Session = Depends(get_psql_db)):
    # Create an instance of the SQLAlchemy model using the Pydantic model's attributes
    new_affiliate = Affiliate_DB(
        name=affiliate.name,
        commission_rate=affiliate.commition_rate,
        commission=affiliate.commission,
    )

    # Add the instance to the database session
    db.add(new_affiliate)
    db.commit()
    db.refresh(new_affiliate)

    return {"affiliate_id": new_affiliate.id}


@routers.get("/get_all_affiliate")
def get_all_affiliate(db: Session = Depends(get_psql_db)):
    all_affiliate = db.query(Affiliate_DB).all()
    if all_affiliate is not None:
        return all_affiliate

    return {"error": "could not have any Affiliate"}


 
@routers.post("/create_product", status_code=status.HTTP_201_CREATED)
def create_product(product: Product, db: Session = Depends(get_psql_db)):
    
    new_product = Product_DB(
        name = product.name,
        affiliate_id = product.affiliate_id,
        product_price = product.product_price,
    )
    try:

        db.add(new_product)
        db.commit()
        db.refresh(new_product)

    except Exception as e:
        print(e, "ssssssssssssssssssssssss")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"product": new_product}


@routers.post('/buy_product/{id}/{product_id}/{product_price}')
def buy_product(id:str, product_id:int,product_price:float,affiliate: Affiliate, db:Session=Depends(get_psql_db)):
    product = db.query(Product_DB).filter(Product_DB.product_id==product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='product not found')
    affiliate_check = db.query(Affiliate_DB).filter(Affiliate_DB.id == id).first()
    if not affiliate_check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='link not found')
    commission_rate = affiliate_check.commission_rate
    commission = product_price * commission_rate
    affiliate_check.commission += commission
    db.commit()
    return {"message": "commission updated successfully"}

@routers.get('get_total_commission/{id}')
def get_total_commission(id:str,db:Session=Depends(get_psql_db)):
    affiliate = db.query(Affiliate_DB).filter(Affiliate_DB.id == id ).first()
    if affiliate is not None:
        return {"message": affiliate.commission}

    
        
   


