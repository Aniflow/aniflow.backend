from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/")
async def get_home_page():
    html_content = """
    <html>
        <head>
            <title>Aniflow API</title>
        </head>
        <body>
            <h1>Welcome to the Aniflow API</h1>
            Check out the documentation <a href="/docs">here</a>
            <br>
            Developed by Ben
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)
