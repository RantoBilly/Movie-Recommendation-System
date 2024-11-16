from pydantic import BaseModel


class MovieRecommendationRequest(BaseModel):
    title: str