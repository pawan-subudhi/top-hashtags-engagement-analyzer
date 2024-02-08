from fastapi import FastAPI
from fastapi.routing import APIRouter
from api.endpoints import hashtags_router

app = FastAPI()

app.include_router(hashtags_router.router, prefix="/api")
