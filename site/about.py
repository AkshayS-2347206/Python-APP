import streamlit as st
from PIL import Image

def render_about_page():
    st.title("About")

    image = Image.open("image.jpg")
    st.image(image, use_column_width=True)

    st.markdown("---")
    st.write("Welcome to my Streamlit app!")
    st.write("This app showcases two main features:")

    st.header("1. Image Filters")
    st.write("You can explore various image processing techniques such as thresholding, edge detection, blur, and more.")

    st.header("2. IMDb Movie Rankings")
    st.write("Using web scraping techniques, this app fetches IMDb movie rankings and displays them for users to explore and visualize them.")

    st.markdown("---")
    st.header("How to Use")
    st.write("1. Select the 'Image' option from the sidebar to access image filtering functionalities.")
    st.write("2. Choose the 'IMDb' option to view the latest IMDb movie rankings.")

    st.markdown("---")
    st.header("Credits")
    st.write("This app was developed by Akshay.")

if __name__ == "__main__":
    render_about_page()
