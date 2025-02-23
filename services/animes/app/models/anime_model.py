from pydantic import BaseModel


class Anime(BaseModel):
    id: int
    title: str
    description: str


sample_animes = [
    Anime(
        id=1,
        title="Attack on Titan",
        description="Humanity fights against giant titans."
    ),
    Anime(
        id=2,
        title="Death Note",
        description="A school student gets a notebook with deadly power."
    ),
    Anime(
        id=3,
        title="Fullmetal Alchemist: Brotherhood",
        description="Two brothers use alchemy to restore their bodies."
    )
]
