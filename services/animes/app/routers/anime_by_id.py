from fastapi import APIRouter

router = APIRouter()


@router.get("/anime/{anime_id}")
async def get_anime(anime_id: int):
    return NotImplemented
