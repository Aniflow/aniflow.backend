from fastapi import APIRouter
from ..models import Anime

router = APIRouter()


@router.get("/animes")
async def get_animes():
    return [
        Anime(
            id=1,
            title="Attack on Titan",
            description="Humanity fights against giant titans."
        ),
        Anime(
            id=2,
            title="Death Note",
            description="A school student gets a notebook with deadly power."),
        Anime(
            id=3,
            title="Fullmetal Alchemist: Brotherhood",
            description="Two brothers use alchemy to restore their bodies.")
    ]
