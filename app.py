import streamlit as st
import pandas as pd
from recommender import MovieRecommender

# Initialize recommender
recommender = MovieRecommender("data/movies.csv", "data/ratings.csv")

# Page Config
st.set_page_config(page_title="🎬 Movie Recommender System", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-image: url('image.png'); /* Replace with your background image URL */
        background-size: cover;
        background-position: center;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .stSelectbox label {
        color: white;
    }
    .recommendation-card {
        background: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
st.write("Select a movie to get similar recommendations!")

# Dropdown for movie selection
movie_list = recommender.movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendation"):
    recommendations = recommender.recommend(selected_movie, top_n=5)
    if len(recommendations) > 0:
        st.subheader("Recommended Movies:")
        cols = st.columns(5)  # Adjust number of columns based on top_n
        for i, row in enumerate(recommendations.itertuples()):
            with cols[i % 5]:
                st.markdown(f'<div class="recommendation-card">', unsafe_allow_html=True)
                # Placeholder for image (replace with actual poster URL logic)
                st.image("https://via.placeholder.com/150", caption=row.title, use_column_width=True)
                st.caption(row.genres)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("No recommendations found!")