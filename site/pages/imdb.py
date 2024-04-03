import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd

numbers = []
titles = []
years = []
runtimes = []
ratings = []
votes = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base").find_all('li', class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")

    for movie in movies:
        name = movie.find('div', class_="sc-b0691f29-0 jbYPfh cli-children").a.h3.text
        number, title = name.split('. ', 1)

        year = movie.find('div', class_="sc-b0691f29-7 hrgukm cli-title-metadata").span.text

        runtime_element = movie.find('div', class_="sc-b0691f29-7 hrgukm cli-title-metadata").find_all('span', class_='cli-title-metadata-item')[1]
        runtime = runtime_element.text

        rating = movie.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.split('(')[0].strip()
        vote = movie.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.split('(')[1].replace(')', '').strip()

        numbers.append(number)
        titles.append(title)
        years.append(year)
        runtimes.append(runtime)
        ratings.append(rating)
        votes.append(vote)

    movie_data = {
        "Number": numbers,
        "Title": titles,
        "Year": years,
        "Runtime": runtimes,
        "Rating": ratings,
        "Votes": votes
    }
    df = pd.DataFrame(movie_data)

    st.title("Top Rated Movies on IMDb")

    min_rating = st.sidebar.slider("Minimum Rating", min_value=0.0, max_value=10.0, step=0.1, value=0.0)

    filtered_df = df[df['Rating'].astype(float) >= min_rating]

    st.dataframe(filtered_df, height=800, width=1200)

    st.subheader("Rating Distribution")
    rating_counts = filtered_df['Rating'].value_counts()
    st.bar_chart(rating_counts)

except Exception as e:
    st.error(f"An error occurred: {e}")
