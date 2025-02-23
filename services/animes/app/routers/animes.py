from fastapi import APIRouter
from ..models import Anime
from ..models import sample_animes

router = APIRouter()


@router.get("/animes", response_model=list[Anime])
async def get_animes():
    return sample_animes
