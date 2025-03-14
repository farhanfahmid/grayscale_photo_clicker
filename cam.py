import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    cam_image = st.camera_input("Camera")
    print(cam_image)

if cam_image:
    img = Image.open(cam_image) #create a pillow image instance
    gray_img = img.convert("L") #L converts image to grayscale
    st.image(gray_img) #render grayscale image on webpage
