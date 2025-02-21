import os

from dotenv import load_dotenv
from fastapi import APIRouter
import httpx

load_dotenv()
router = APIRouter()

user_service_url = os.getenv("USER_SERVICE_URL")


@router.get("/user/{user_id}")
async def get_user_endpoint(user_id: int):
    """
    Fetch a user by their unique user ID.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        dict: The user data, including user ID and name, if found.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'{user_service_url}/users/{user_id}'
        )
    return response.json()
