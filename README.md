# Ai-Movie-Recommender

 📌 Overview:
 
Users can input a movie title, and the system will suggest similar movies based on genre similarity (Content-Based Filtering). The recommendations are displayed via a clean and intuitive Streamlit UI.

📂 Dataset
We use the MovieLens Small Dataset, which includes:
- movies.csv: Movie titles and genres
- ratings.csv: User ratings for movies

📊 Data Exploration
Basic insights extracted using Pandas:



Top 5 Movies by Rating Count:
- Forrest Gump (1994)
- Pulp Fiction (1994)
- Shawshank Redemption, The (1994)
- Silence of the Lambs, The (1991)
- Matrix, The (1999)

🧠 Recommendation Logic
🔍 Method: Content-Based Filtering
We recommend movies based on genre similarity using cosine similarity between genre vectors.
Steps:
- Preprocess genres into one-hot encoded vectors.
- Compute similarity matrix using cosine similarity.
- Recommend top 5 movies most similar to the input movie.

💻 User Interface
Built using Streamlit, the UI allows users to:
- Input or select a movie title
- View 5 recommended movies
- See results in a clean, readable format (list/table)
✅ Tested With:
- The Dark Knight
- Titanic
- Toy Story





