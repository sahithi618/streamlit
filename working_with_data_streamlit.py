import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import cv2 as cv

st.title('1. Image from path')
img=Image.open(r"C:\Users\HP\OneDrive\Documents\streamlit\img.png")
st.image(img)

st.title('2. Image from link')
st.image('https://media.geeksforgeeks.org/gfg-gg-logo.svg',width=500)


st.title('3. Audio')
audio_file=open(r"C:\Users\HP\OneDrive\Documents\streamlit\song.mp3",'rb')
st.audio(audio_file,start_time=20)#same goes for video as st.video

df=pd.read_csv(r"C:\Users\HP\OneDrive\Documents\streamlit\Products.csv")
st.subheader('Displaying dataframe')
st.dataframe(df.head(10))
st.table(df.head())#Table format
st.write(df.describe())

st.title('Image Converter')
def convert_image(img_path,new_format):
    with Image.open(img_path) as img:
        new_name=img_path.name.split('.')[0]+'.'+new_format
        final_path="C:\\Users\\HP\\OneDrive\\Documents\\streamlit\\" + new_name

        st.write(final_path)
        img.save(final_path)


img_path=st.file_uploader('Upload your image file',type=['jpg','jpeg','png'])

new_format=st.selectbox('Select the output format',['jpg','jpeg','png'])

if st.button('Convert'):
    if img_path is not None:
        convert_image(img_path,new_format)
    else:
        st.error("Please upload a file")

st.title("Image Rotator")
def rotate_image(image, angle):
    img = np.array(image)
    height, width = img.shape[:2]
    M = cv.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_img = cv.warpAffine(img, M, (width, height))
    return rotated_img

st.subheader('Rotate the image')
rotated_angle=st.slider("Select the angle required",-180,180,0,1)
if img_path is not None:
    image=Image.open(img_path)
    rotated_img=rotate_image(image,rotated_angle)
    st.image(rotated_img)