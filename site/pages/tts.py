import streamlit as st
import requests
import pyttsx3

def get_movie_data(movie_name, api_key):
    url = f"http://www.omdbapi.com/?apikey={'34bd57c6'}&t={movie_name}&plot=full"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error fetching movie data. Please try again later.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return None

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(f"Error in text-to-speech conversion: {e}")

st.title("Movie Description and Text-to-Speech")

movie_name = st.text_input("Enter a movie name:")

api_key = "34bd57c6"

if st.button("Get Movie Description"):
    if movie_name:
        movie_data = get_movie_data(movie_name, api_key)
        if movie_data and movie_data.get('Response') == 'True':
            st.subheader(movie_data['Title'])
            st.image(movie_data['Poster'], caption='Movie Poster', use_column_width=True)
            st.write(f"Release Date: {movie_data['Released']}")
            st.write(f"Overview: {movie_data['Plot']}")

            if st.button("Text-to-Speech"):
                text_to_speech(movie_data['Plot'])
        else:
            st.error("Movie not found. Please check the spelling or try another movie.")
    else:
        st.warning("Please enter a movie name.")