import streamlit as st
import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# --------- CUSTOM CSS ---------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(180deg, #0b0b0b 0%, #111111 50%, #0b0b0b 100%);
}


/* Title */
h1 {
    color: #FFFFFF !important;
    opacity: 1 !important;
    text-align: center;
    font-size: 7rem;
    text-shadow: 0 0 6px rgba(229,9,20,0.6);
}



/* Selectbox */
div[data-baseweb="select"] {
    color: #FFFFFF !important;
    background-color: #111111;
    border-radius: 10px;
    border: 1px solid #2a2a2a;
}
label {
    color: #FFFFFF !important;
    opacity: 1 !important;
    font-size: 3rem;
    font-weight: 500;
}


/* Button */
.stButton>button {
    background: linear-gradient(135deg, #E50914, #ff003c);
    color: white;
    border-radius: 25px;
    height: 3em;
    width: 200px;
    font-size: 16px;
    box-shadow: 0 0 15px #E50914;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0 0 30px #ff003c;
    transform: scale(1.05);
}

/* Movie cards */
.movie-card {
    background: #111;
    border-radius: 15px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 0 20px rgba(255,0,60,0.4);
    transition: 0.3s;
}

.movie-card:hover {
    transform: scale(1.08);
    box-shadow: 0 0 40px rgba(255,0,60,0.8);
}

.movie-title {
    color: white;
    font-weight: bold;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)

import pickle
import requests
import pandas as pd


# Load precomputed movie data and cosine similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get top 10 similar movies
def get_recommendations(title, cosine_sim=cosine_sim):
    # Find index of the movie in the dataset
    idx = movies[movies['title'] == title].index[0]
    
    # Get similarity scores for this movie with all others
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort movies based on similarity score (descending)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 10 similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:11]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Return movie titles and their IDs
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Function to fetch movie poster using TMDB API
def fetch_poster(movie_id):
    api_key = '501029f1226bd4c3289d9461f17ac63f'  
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    
    # Send request to TMDB API
    response = requests.get(url)
    
    # Convert response to JSON
    data = response.json()
    
    # Get poster path from API response
    poster_path = data.get('poster_path', None)
    
    if poster_path:
        # Construct full URL for poster image
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_path
    else:
        return None  # Return None if no poster found

st.title("Movie Recommendation system")
selected_movie = st.selectbox("Select a movie:", movies['title'].values)
# Recommend button
if st.button("Recommend"):
    # Get top 10 recommendations for the selected movie
    recommendation = get_recommendations(selected_movie)
    st.write("Top 10 Recommended Movies:")
    

    # Create a 2x5 grid layout
    for i in range(0, 10, 5):
        # Create 5 columns for each row
        columns = st.columns(5)
        for col, j in zip(columns, range(i, i + 5)):
            movie_title = recommendation.iloc[j]["title"]
            movie_id = recommendation.iloc[j]["movie_id"]
            poster_url = fetch_poster(movie_id)
            
            # Display poster and title in the column
            with col:
                st.image(poster_url, width=130)
                st.write(movie_title)
