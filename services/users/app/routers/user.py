from fastapi import APIRouter, HTTPException
from ..models import User
from ..models import sample_users

router = APIRouter()


@router.get("/user/{user_id}", response_model=User)
async def get_anime(user_id: int):
    for user in sample_users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Anime not found")
