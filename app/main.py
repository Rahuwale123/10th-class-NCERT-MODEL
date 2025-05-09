from fastapi import FastAPI
from app.api.routes import router
from app.config import API_TITLE, API_DESCRIPTION

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION
)

app.include_router(router) 