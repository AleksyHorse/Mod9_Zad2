from unittest.mock import Mock

from main import app
import tmdb_client

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('https://api.themoviedb.org/3/movie/popular')

def test_movie_details():
   with app.test_client() as client:
       response = client.get('/movie/583')
       assert response.status_code == 200