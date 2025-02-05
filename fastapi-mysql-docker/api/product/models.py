from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    Queue:  Optional[str] = None
    order_id: Optional[str] = None
    cust_id: Optional[str] = None
    order_Date: str
    booktime: str
