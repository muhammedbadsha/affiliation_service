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
    
    # sql_statement = text(
    #     "INSERT INTO products (name, affiliate_id, product_price) "
    #     "VALUES (:name, :affiliate_id, :product_price) "
    #     "RETURNING products.created_at"
    # )

    
    # result = db.execute(sql_statement, {
    #     'name': product.name,
    #     'affiliate_id': [str(aff_id) for aff_id in product.affiliate_id],
    #     'product_price': product.product_price
    # }).fetchone()
        
   


