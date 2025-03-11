import pytest
from fastapi.testclient import TestClient
from services.animes.app.main import app
from services.animes.app.models import Anime


@pytest.fixture
def mock_sample_animes(monkeypatch):
    mock_animes = [
        Anime(id=1, title="Naruto", description="Ninja adventure"),
        Anime(id=2, title="One Piece", description="Pirate adventures")
    ]

    monkeypatch.setattr(
        "services.animes.app.models.anime_model.sample_animes",
        mock_animes
    )

    return mock_animes


def test_get_anime_found(mock_sample_animes):
    client = TestClient(app)

    response = client.get("/anime/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Attack on Titan",
        "description": "Humanity fights against giant titans."
    }


def test_get_anime_not_found(mock_sample_animes):
    client = TestClient(app)

    response = client.get("/anime/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Anime not found"}
