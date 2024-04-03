import cv2
import numpy as np
import streamlit as st
from PIL import Image

def apply_filters(image, filter_option, parameters=None):
    if filter_option == "Original Image":
        return image
    elif filter_option == "Grayscale":
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return grayscale_image
    elif filter_option == "Blur":
        blurred_image = cv2.GaussianBlur(image, (7, 7), 0)
        return blurred_image
    elif filter_option == "Edge Detection":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edge_image = cv2.Canny(gray, 100, 200)
        return edge_image
    elif filter_option == "Resize":
        resized_image = cv2.resize(image, (parameters["width"], parameters["height"]))
        return resized_image
    elif filter_option == "Rotate":
        rotation_matrix = cv2.getRotationMatrix2D((image.shape[1]/2, image.shape[0]/2), parameters["angle"], 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
        return rotated_image
    elif filter_option == "Flip":
        flipped_image = cv2.flip(image, parameters["flip_code"])
        return flipped_image

def main():
    st.title("Image Processing and Filtering")

    st.sidebar.header("Choose an Option")
    filter_option = st.sidebar.selectbox(
        "Filter",
        ["Original Image", "Grayscale", "Blur", "Edge Detection", "Resize", "Rotate", "Flip"]
    )

    if filter_option in ["Resize", "Rotate", "Flip"]:
        if filter_option == "Resize":
            width = st.sidebar.number_input("Enter Width", min_value=1)
            height = st.sidebar.number_input("Enter Height", min_value=1)
            parameters = {"width": width, "height": height}
        elif filter_option == "Rotate":
            angle = st.sidebar.slider("Angle", min_value=0, max_value=360, value=0)
            parameters = {"angle": angle}
        elif filter_option == "Flip":
            flip_code_options = {"Horizontal": 1, "Vertical": 0, "Both": -1}
            flip_code = st.sidebar.radio("Flip Direction", list(flip_code_options.keys()))
            parameters = {"flip_code": flip_code_options[flip_code]}
    else:
        parameters = None

    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)
        image = np.array(pil_image)

        filtered_image = apply_filters(image, filter_option, parameters)

        st.image(filtered_image, caption=filter_option, use_column_width=True)

if __name__ == "__main__":
    main()
