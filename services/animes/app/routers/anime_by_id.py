from fastapi import APIRouter, HTTPException
from ..models import Anime
from ..models import sample_animes

router = APIRouter()


@router.get("/anime/{anime_id}", response_model=Anime)
async def get_anime(anime_id: int):
    for anime in sample_animes:
        if anime.id == anime_id:
            return anime
    raise HTTPException(status_code=404, detail="Anime not found")
