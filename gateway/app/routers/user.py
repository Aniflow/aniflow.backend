from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/user")
async def get_user():
    return HTMLResponse(content=NotImplemented, status_code=status.HTTP_200_OK)
