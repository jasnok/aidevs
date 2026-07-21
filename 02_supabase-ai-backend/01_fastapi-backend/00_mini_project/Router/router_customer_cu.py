"""
uvicorn 00_request:app --reload
"""


from fastapi import APIRouter, HTTPException
from Schema.model_common import ApiResponse
from model_customer import Customer


router_cu = APIRouter()


@router_cu.get("/health")
def health():
    response = ApiResponse(
        success=True,
        message="OK",
    )
    return response

# Request Body
# insert, update
@router_cu.put("/update")
async def update(customer:Customer):
    print(customer.id)
    print(customer.name)
    print(customer.age)
    if customer.id == "id88":
        raise HTTPException(status_code=404, detail="ID가 존재 안함")
    # await print("수정 진행...")
    response = ApiResponse(
        success = True,
        message = f"{customer.name} 수정 완료!",
        data = customer
    )
    return response


@router_cu.post("/register")
async def register(customer:Customer):
    print(customer.id)
    print(customer.name)
    print(customer.age)
    response = None
    response = ApiResponse(
        success = True,
        message = f"{customer.name} 가입축하!",
    )
    return response
