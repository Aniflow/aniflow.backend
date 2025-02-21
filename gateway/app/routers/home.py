import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "../static")
INDEX_FILE = os.path.join(STATIC_DIR, "index.html")


@router.get("/")
async def get_home_page():
    """Serve index.html as homepage"""
    return FileResponse(INDEX_FILE)
