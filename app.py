import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=fed9e3541264da1937a6aefbee0cdf56&language=en-US")
    data = response.json()
    poster_path = data["poster_path"]
    return "https://image.tmdb.org/t/p/w500/"+poster_path



def recommend(movie):
    
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]


    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list :
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies = pickle.load(open("movies.pkl","rb"))

similarity = pickle.load(open("similarity.pkl","rb"))


st.title("Movie Recomender System")

selected_movie_name = st.selectbox(
    "Select the movie name ",
    movies["title"].values
)

if st.button("Recommend") :
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.markdown(f"<p style='font-size:14px; text-align:center; font-weight:600'>{names[0]}</p>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f"<p style='font-size:14px; text-align:center; font-weight:600'>{names[1]}</p>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<p style='font-size:14px; text-align:center; font-weight:600'>{names[2]}</p>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<p style='font-size:14px; text-align:center; font-weight:600'>{names[3]}</p>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<p style='font-size:14px; text-align:center; font-weight:600'>{names[4]}</p>", unsafe_allow_html=True)
        st.image(posters[4])
