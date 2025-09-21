import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, movies_file, ratings_file=None):
        self.movies = pd.read_csv(movies_file)
        self.ratings = pd.read_csv(ratings_file) if ratings_file else None
        self.similarity_matrix = None
        self._prepare()

    def _prepare(self):
        # Fill missing genres
        self.movies['genres'] = self.movies['genres'].fillna('')
        
        # Convert genres to TF-IDF matrix
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies['genres'])
        
        # Compute cosine similarity
        self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def recommend(self, title, top_n=5):
        if title not in self.movies['title'].values:
            return []
        
        idx = self.movies[self.movies['title'] == title].index[0]
        scores = list(enumerate(self.similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        
        recommended_idx = [i[0] for i in scores[1:top_n+1]]
        return self.movies.iloc[recommended_idx][['movieId', 'title', 'genres']]
