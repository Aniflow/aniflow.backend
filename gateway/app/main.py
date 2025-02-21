from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import anime_router
from .routers import home_router
from .routers import user_router

app = FastAPI(title="Aniflow API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(anime_router)
app.include_router(home_router)
app.include_router(user_router)
