import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def api(monkeypatch):
    test_films = [{"id": 1, "name": "Eternal Sunshine of the spotless mind", "genre": "Drama", "release_date": 2004}, 
                  {"id": 2, "name": "Mullholland Dr", "genre": "Thriller", "release_date": 2001}, 
                  {"id": 3, "name": "Howl'\s Moving Castle", "genre": 'Adventure', "release_date": 2004}]
    monkeypatch.setattr(server, "films", test_films)
    api = server.app.test_client()
    return api
