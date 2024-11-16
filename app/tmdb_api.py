import requests


class TMDBClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.themoviedb.org/3'

    def get_movie_details(self, title):
        response = requests.get(f"{self.base_url}/search/movie", params={"api_key": self.api_key, "query": title})
        if response.status_code == 200:
            return response.json()['results'][0]
        return None
