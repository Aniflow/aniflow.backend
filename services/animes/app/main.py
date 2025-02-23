from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import animes_router
from .routers import anime_router

app = FastAPI(title="Aniflow Anime Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(animes_router)
app.include_router(anime_router)
