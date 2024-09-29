import requests

base_url = "https://api.kinopoisk.dev/v1.4"
key = "FFVW3FK-F6PMTZW-G52F6R6-179PNR9"

def search_movie_by_title():
    headers = {
    "X-API-KEY" : "key"
    }
    response = requests.get(base_url+'/movie/search?page=1&limit=10&query=экипаж', headers=headers)
    response_body = response.json()
    first_movie = response_body[0]
    assert first_movie ["name"] == "Экипаж"
    assert response.status_code == 200
