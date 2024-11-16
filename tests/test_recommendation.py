import unittest
from app.recommendation import RecommendationEngine
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '..', 'data', 'processed', 'preprocessed_data.csv')


class TestRecommendationEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = RecommendationEngine(data_path='data/processed/preprocessed_data.csv')

    def test_recommend_movie(self):
        result = self.engine.recommend_movie("Avatar")
        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()
