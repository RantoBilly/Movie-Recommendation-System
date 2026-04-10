from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import recommendation_router
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# setting up CORS Middleware : access from localhost:8001 authorized
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods= ['*'],
    allow_headers= ['*'],

)

# Routes API en premier (priorité sur les fichiers statiques)
app.include_router(recommendation_router.router)

# Frontend servi comme fichiers statiques (catch-all)
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

@app.get("/")
def read_root():
    return {"message": "Recosphere TechLab 2024"}