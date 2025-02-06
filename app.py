import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Function to convert image to sketch
def convert_to_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    return sketch

# Streamlit App
st.title("Image to Sketch Converter 🎨✏️")
st.write("Upload an image, and I'll turn it into a pencil sketch!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
    image = Image.open(uploaded_file)
    image = np.array(image)  # Convert to numpy array
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV processing

    # Display original image
    st.image(image, caption="Original Image", use_container_width=True)

    # Convert to sketch
    sketch = convert_to_sketch(image)

    # Display the sketch
    st.image(sketch, caption="Pencil Sketch", use_container_width=True, clamp=True)

    # Provide option to download the sketch
    # sketch_pil = Image.fromarray(sketch)
    # st.download_button("Download Sketch", data=sketch_pil.tobytes(), file_name="sketch.png", mime="image/png")

    

# Convert the sketch to a downloadable format
    sketch_pil = Image.fromarray(sketch)
    buffer = BytesIO()
    sketch_pil.save(buffer, format="PNG")
    buffer.seek(0)

# Provide a working download button
    st.download_button(
    label="Download Sketch",
    data=buffer,
    file_name="sketch.png",
    mime="image/png")

