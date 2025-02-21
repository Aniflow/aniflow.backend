from fastapi import FastAPI

from routers.anime import router as anime_router
from routers.home import router as home_router
from routers.user import router as user_router

app = FastAPI(title="API Gateway")

app.include_router(anime_router)
app.include_router(home_router)
app.include_router(user_router)
