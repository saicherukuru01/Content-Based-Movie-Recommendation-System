
import streamlit as st
import pickle
import pandas as pd

st.title('🎬 Movie Recommender System')

# Load Data
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# UI Controls
selected_movie = st.selectbox('Select a movie you like:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write("### You might also like:")
    for movie in recommendations:
        st.write(f"⭐ {movie}")
