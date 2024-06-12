import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# URL을 통해 이미지 불러오기
response = requests.get('https://path-to-your-image.jpg')
image = Image.open(BytesIO(response.content))

# Streamlit에 이미지 삽입
st.image(image, caption='Your Caption Here', use_column_width=True)
