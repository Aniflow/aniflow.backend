from fastapi import FastAPI

from routers import anime_router
from routers import home_router
from routers import user_router

app = FastAPI(title="API Gateway")

app.include_router(anime_router)
app.include_router(home_router)
app.include_router(user_router)
