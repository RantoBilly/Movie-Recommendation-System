import pandas as pd
import ast


def preprocess_data(movies_path, credits_path, output_path):
    movies_6000 = pd.read_csv(movies_path)
    credits_6000 = pd.read_csv(credits_path)

    movies_6000.drop(columns='Unnamed: 0', inplace=True)
    movies_6000.rename(columns={'tmdbId': 'id'}, inplace=True)
    credits_6000.drop(columns='Unnamed: 0', inplace=True)
    credits_6000.rename(columns={'tmdbId': 'movie_id'}, inplace=True)
    credits_6000['title'] = movies_6000['title']

    data = movies_6000.merge(credits_6000, on='title')
    my_data = data[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew', 'production_companies']]
    my_data.dropna(inplace=True)

    def convert(text):
        return [i['name'] for i in ast.literal_eval(text)]
    
    def convert_crew(text):
        return [i['name'] for i in ast.literal_eval(text) if i['job'] == 'Director']

    def convert_cast(text):
        return [i['name'] for i in ast.literal_eval(text)[:3]]

    my_data['genres'] = my_data['genres'].apply(convert)
    my_data['keywords'] = my_data['keywords'].apply(convert)
    my_data['production_companies'] = my_data['production_companies'].apply(convert)
    my_data['cast'] = my_data['cast'].apply(convert_cast)
    my_data['crew'] = my_data['crew'].apply(convert_crew)

    def combine_features(row):
        return " ".join(row['genres']) + " " + " ".join(row['keywords']) + " " + " ".join(row['cast']) + " " + " ".join(
            row['crew']) + " " + " ".join(row['production_companies']) + " " + row['overview']

    my_data['tags'] = my_data.apply(combine_features, axis=1)

    my_data.to_csv(output_path, index=False)