from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
#Product เรียกใช้โฟลเดอร์พร้อมไฟล์ข้างใน
from product import ProductModel,get_all_product,get_product_by_id,add_product,update_product,delete_product


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ##GET
@app.get("/get_all_product/", response_model=list[ProductModel])
def get_all_product_api():
    products = get_all_product()
    print(products)
    return JSONResponse(status_code=200, content=jsonable_encoder(products))

@app.get("/get_product/{Queue}", response_model=ProductModel)
def get_product_by_id_api(Queue:str):
    products = get_product_by_id(Queue)
    return JSONResponse(status_code=200, content=jsonable_encoder(products))

#Post Create
@app.post('/create_product/', response_model=ProductModel)
def create_product_api(product: ProductModel):
    Queue = add_product(product)
    return JSONResponse(status_code=201, content={'status': 'success', 'product_id': Queue})

#Update
@app.put("/update_product/{Queue}", response_model=ProductModel)
def update_product_api(Queue: str, product: ProductModel):
    # Check if product exists
    existing_product = get_product_by_id(Queue)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_product = update_product(Queue, product)
    if updated_product:
        return JSONResponse(status_code=200, content={'status': 'success', 'product_data': updated_product})
    else:
        raise HTTPException(status_code=500, detail="Failed to update data")
    
#Delete
@app.delete("/delete_product/{Queue}", response_model=ProductModel)
def delte_product_api(Queue: str):
    existing_product = get_product_by_id(Queue)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_product(Queue)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")

