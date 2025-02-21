import pytest
from httpx import AsyncClient
from gateway.app.main import app


@pytest.mark.asyncio
async def test_get_home_page():
    """Test the home page response"""

    expected_content = """
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
    """.strip()

    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.text.strip() == expected_content
