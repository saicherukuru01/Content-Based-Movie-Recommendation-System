# 🎬 Movie Recommender System

A content-based movie recommendation system using Machine Learning. 
This application recommends movies similar to the one a user likes by analyzing movie tags (genres, keywords, cast, and crew) using **Cosine Similarity**.

## 🔧 Technologies Used
* **Python** (Core language)
* **Pandas** (Data manipulation)
* **Scikit-Learn** (Machine Learning: CountVectorizer, Cosine Similarity)
* **Streamlit** (Frontend Web App)

## 📊 How it Works
1.  **Data Processing:** The system merges the TMDB 5000 Movies and Credits datasets.
2.  **Feature Engineering:** It combines the movie overview, genre, keywords, cast, and crew into a single "tags" column.
3.  **Vectorization:** Text data is converted into numerical vectors using `CountVectorizer`.
4.  **Similarity Calculation:** It calculates the cosine distance between vectors to find the most similar movies.

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR-USERNAME/movie-recommender-system.git](https://github.com/YOUR-USERNAME/movie-recommender-system.git)
cd movie-recommender-system
## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone [https://github.com/saicherukuru01/Content-Based-Movie-Recommendation-System.git](https://github.com/saicherukuru01/Content-Based-Movie-Recommendation-System.git)
cd Content-Based-Movie-Recommendation-System
