from fastapi import FastAPI

# examples
from app.api.api_router import api_router


app = FastAPI()

app.include_router(api_router, prefix="/api")
