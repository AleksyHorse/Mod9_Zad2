import requests
import random


api_token="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjU0OGUyZDE4NTA3ZTBkN2FhYzcyZWJlMGFlMTBiZiIsInN1YiI6IjYyNmZlOGM1ZDEzMzI0MTEzZTJjODFiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.62L9nLRjTwwrgNq5pPcLrSJ8Pd3NaUEYcEPCYXidYpA"
headers = {
        "Authorization": f"Bearer {api_token}"
    }
def call_tmdb_api(endpoint):
   full_url = f"{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_poster_url(_path, size="w342"):
    return f"https://image.tmdb.org/t/p/{size}/{_path}" 

def random_get_backdrop(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    backs = call_tmdb_api(endpoint)["backdrops"]
    chosen = random.choice(backs)
    print(chosen)
    return chosen

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    return call_tmdb_api(endpoint)["cast"]

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    return call_tmdb_api(endpoint)

def get_movies_list(list_name):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return call_tmdb_api(endpoint)

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    return call_tmdb_api(endpoint)

def get_movies(how_many,kind="popular"):
    data = get_movies_list(kind)["results"]
    random.shuffle(data)
    return data[:how_many]