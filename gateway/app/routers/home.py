import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, "../static")
index_file = os.path.join(static_dir, "index.html")


@router.get("/")
async def get_home_page():
    """Serve index.html as homepage"""
    return FileResponse(index_file)
