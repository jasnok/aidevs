from fastapi import FastAPI
from app.routers.chat_router import chat_router
from app.routers.product_router import product_router
from app.core import chat_config  # load_dotenv() 실행

app = FastAPI(title="Main App")

app.include_router(chat_router)
app.include_router(product_router)