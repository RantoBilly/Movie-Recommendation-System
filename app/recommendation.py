import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process


class RecommendationEngine:
    def __init__(self, data_path):
        self.my_data = pd.read_csv(data_path)
        self.my_data['tags'] = self.my_data['tags'].fillna('')
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.my_data['tags'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        self.indices = pd.Series(self.my_data.index, index=self.my_data['title']).drop_duplicates()

    def recommend_movie(self, title):
        title = title.lower()
        best_match = process.extractOne(title, self.indices.index)
        if best_match[1] < 80:
            return ['Movie not found in the dataset']

        idx = self.indices[best_match[0]]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return self.my_data['title'].iloc[movie_indices].tolist()