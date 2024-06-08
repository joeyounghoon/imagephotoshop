import streamlit as st
from PIL import Image, ImageEnhance
import openai

def generate_edit_instructions(api_key, prompt):
    openai.api_key = api_key
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates image editing instructions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].message['content'].strip()

def edit_image(image, instructions):
    instructions = instructions.lower()
    edited_image = image

    if "brightness" in instructions:
        factor = 1.5  # 기본 밝기 증가 배율
        if "increase" in instructions:
            factor = 1.5
        elif "decrease" in instructions:
            factor = 0.5
        enhancer = ImageEnhance.Brightness(edited_image)
        edited_image = enhancer.enhance(factor)

    if "crop" in instructions:
        width, height = edited_image.size
        left = width * 0.1
        top = height * 0.1
        right = width * 0.9
        bottom = height * 0.9
        edited_image = edited_image.crop((left, top, right, bottom))

    return edited_image

# Streamlit 파일 업로드 및 프롬프트 입력
st.title("AI 포토샵 웹앱")
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])
prompt = st.text_input("편집 지침을 입력하세요")
api_key = st.text_input("OpenAI API 키를 입력하세요", type="password")

if uploaded_file and prompt and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption='원본 이미지')

    instructions = generate_edit_instructions(api_key, prompt)
    st.write(f"생성된 편집 지침: {instructions}")

    edited_image = edit_image(image, instructions)
    st.image(edited_image, caption='편집된 이미지')
