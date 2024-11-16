from app.data_preprocessing import preprocess_data
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

movies_path = os.path.join(current_dir, '..', 'data', 'raw', 'tmdb_6000_movie_dataset.csv')
credits_path = os.path.join(current_dir, '..', 'data', 'raw', 'tmdb_6000_movie_credits.csv')
output_path = os.path.join(current_dir, '..', 'data', 'processed', 'preprocessed_data.csv')

preprocess_data(
    movies_path=movies_path,
    credits_path= credits_path,
    output_path= output_path
)