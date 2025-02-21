import os

from dotenv import load_dotenv
from fastapi import APIRouter
import httpx

load_dotenv()
router = APIRouter()

anime_service_url = os.getenv("ANIME_SERVICE_URL")


@router.get("/anime/{anime_id}")
async def get_anime_endpoint(anime_id: int):
    """
    Fetch an anime by its unique anime ID.

    Args:
        anime_id (int): The unique identifier of the anime.

    Returns:
        dict: The anime data, including anime ID and title, if found.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'{anime_service_url}/animes/{anime_id}'
        )
    return response.json()
