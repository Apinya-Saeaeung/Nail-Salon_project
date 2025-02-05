from fastapi import HTTPException,APIRouter
from database.query import query_get, query_create, query_update

from .models import ProductModel

def get_all_product():
    products = query_get("""
        SELECT  
            *
        FROM Booking
        """, ())
    return products

def get_product_by_id(Queue: str):
    product = query_get("""
        SELECT
            *
        FROM Booking
        WHERE Queue = %s
        """, (Queue))
    return product

def add_product(product: ProductModel):
    last_row_id = query_create("""
                INSERT INTO Booking (
                    Queue,
                    order_id,
                    cust_id,
                    order_Date,
                    booktime
                ) VALUES (%s, %s, %s, %s,%s)
                """,
                (
                    product.Queue,
                    product.order_id,
                    product.cust_id,
                    product.order_Date,
                    product.booktime
                )
                )
    return last_row_id

def update_product(Queue: str,product: ProductModel):
    is_update = query_update("""
            UPDATE Booking
                SET order_id = %s,
                cust_id = %s,
                order_Date = %s,          
                booktime = %s
                WHERE Queue = %s;
            """,
            (
                product.order_id,
                product.cust_id,
                product.order_Date,
                product.booktime,
                Queue
            )
            )
    if is_update:
        product_update_data = product.dict()
        product_update_data.update({"Queue": Queue})
        return product_update_data
    else:
        return None
    
def delete_product(Queue: str):
    is_deleted = query_update("""
        DELETE FROM Booking
        WHERE Queue = %s;
        """,
        (Queue,)
        )
    return is_deleted