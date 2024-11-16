from fastapi import APIRouter, HTTPException
from app.recommendation import RecommendationEngine
from app.models import MovieRecommendationRequest
from app.config import TMDB_API_KEY
from app.tmdb_api import TMDBClient
import os

router = APIRouter()

# dynamic path
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '..', 'data', 'processed', 'preprocessed_data.csv')

engine = RecommendationEngine(data_path='data/processed/preprocessed_data.csv')
tmdb_client = TMDBClient(api_key=TMDB_API_KEY)


@router.post("/recommend/")
def recommend_movie(request: MovieRecommendationRequest):
    recommendations = engine.recommend_movie(request.title)
    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found")

    result = []
    for movie in recommendations:
        details = tmdb_client.get_movie_details(movie)
        if details:
            result.append({
                "title": movie,
                "poster_url": f"https://image.tmdb.org/t/p/w500{details['poster_path']}"
            })
    return result




