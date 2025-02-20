import ast
import pandas as pd
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentRecommender:
    """A content-based recommendation system using TF-IDF and cosine similarity."""

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = self.load_data()
        self.vectorizer, self.tfidf_matrix = self.vectorize_text()

    def load_data(self):
        """Loads and preprocesses dataset, merging relevant text fields for downstream work."""
        df = pd.read_csv(self.dataset_path)
        df = df[['title', 'overview', 'genres', 'keywords']].dropna()
        df.rename(columns={'overview': 'description'}, inplace=True)

        # Convert genres and keywords from JSON-like strings to readable text
        df['genres'] = df['genres'].apply(
            lambda x: ' '.join([g['name'] for g in ast.literal_eval(x)]) if isinstance(x, str) else '')
        df['keywords'] = df['keywords'].apply(
            lambda x: ' '.join([k['name'] for k in ast.literal_eval(x)]) if isinstance(x, str) else '')

        # Merge text fields into a single description
        df['description'] = df['description'] + ' ' + df['genres'] + ' ' + df['keywords']

        # Keep only 500 movies as required
        df = df.sample(n=500, random_state=42)
        return df

    def vectorize_text(self):
        """Converts movie descriptions into TF-IDF vectors with NLP settings."""

        # Lemmatization function
        lemmatizer = WordNetLemmatizer()

        def preprocess_text(text):
            text = text.lower() # Convert to lowercase
            return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

        # Apply lowercasing + lemmatization
        self.df['description'] = self.df['description'].apply(preprocess_text)

        # TF-IDF Vectorizer with bigrams
        vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=5000,  # Keep only the top 10000 most important words
            max_df=0.85, # Filters out terms that appear in more than 85% of documents
            min_df=2, # Ignores terms that appear in fewer than 2 documents
            ngram_range=(1, 2)  # Use unigrams and bigrams to capture phrases
        )
        tfidf_matrix = vectorizer.fit_transform(self.df['description'])
        return vectorizer, tfidf_matrix

    def get_recommendations(self, query, top_n=3):
        """Returns the top 3 relevant movies to the query with similarity ranking."""
        query_vector = self.vectorizer.transform([query])

        similarity_scores = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        top_indices = similarity_scores.argsort()[-top_n:][::-1]

        return self.df.iloc[top_indices][['title', 'genres', 'keywords']], similarity_scores[top_indices]

