import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_animes(monkeypatch):
    mock_response = [
        {"id": 1, "title": "Attack on Titan"},
        {"id": 2, "title": "Death Note"}
    ]

    class MockResponse:
        status_code = 200

        async def json(self):
            return mock_response

        async def aclose(self):
            pass

    async def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)

    async with AsyncClient(base_url="http://test") as client:
        response = await client.get("/animes")

    assert response.status_code == 200
    assert await response.json() == mock_response


@pytest.mark.asyncio
async def test_get_anime(monkeypatch):
    anime_id = 1
    mock_response = {"id": anime_id, "title": "Attack on Titan"}

    class MockResponse:
        status_code = 200

        async def json(self):
            return mock_response

        async def aclose(self):
            pass

    async def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)

    async with AsyncClient(base_url="http://test") as client:
        response = await client.get(f"/anime/{anime_id}")

    assert response.status_code == 200
    assert await response.json() == mock_response
