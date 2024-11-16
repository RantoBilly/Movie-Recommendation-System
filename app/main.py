from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import recommendation_router

app = FastAPI()

# setting up CORS Middleware : access from localhost:8001 authorized
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8001"],
    allow_credentials = True,
    allow_methods= ['*'],
    allow_headers= ['*'],

)

# including the routers
app.include_router(recommendation_router.router)


@app.get("/")
def read_root():
    return {"message": "Recosphere TechLab 2024"}