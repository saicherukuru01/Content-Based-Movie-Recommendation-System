import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prepare_data():
    print("Loading data...")
    try:
        movies = pd.read_csv('tmdb_5000_movies.csv')
        credits = pd.read_csv('tmdb_5000_credits.csv')
        
        movies = movies.merge(credits, on='title')
        movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        movies.dropna(inplace=True)
        
        movies['tags'] = movies['overview'] + movies['genres']
        new_df = movies[['movie_id', 'title', 'tags']]
        
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(new_df['tags'].values.astype('U')).toarray()
        similarity = cosine_similarity(vectors)
        
        pickle.dump(new_df, open('movies_list.pkl', 'wb'))
        pickle.dump(similarity, open('similarity.pkl', 'wb'))
        print("Model built and saved successfully!")
    except FileNotFoundError:
        print("Error: CSV files not found. Please download tmdb_5000_movies.csv from Kaggle.")

if __name__ == "__main__":
    prepare_data()
