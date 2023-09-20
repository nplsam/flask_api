import json

def test_api_get_films(api):
    res = api.get("/films")
    assert res.json == {"films": [{"id": 1, "name": "Eternal Sunshine of the spotless mind", "genre": "Drama", "release_date": 2004}, {"id": 2, "name": "Mullholland Dr", "genre": "Thriller", "release_date": 2001}, {"id": 3, "name": "Howl'\s Moving Castle", "genre": 'Adventure', "release_date": 2004}]}

def test_api_post_films(api):
    mock_data = json.dumps({"name": "Chinatown", "genre": "Crime", "release_date": 1974})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/films', data=mock_data, headers=mock_headers)
    assert res.json['film']['id'] == 4