from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/anime")
async def get_anime():
    return HTMLResponse(content=NotImplemented, status_code=status.HTTP_200_OK)
