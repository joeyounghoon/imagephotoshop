# 필수 패키지 임포트
import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = 'your-openai-api-key'

# Streamlit 애플리케이션 제목
st.title("OpenAI API Assistant Bot")

# 사용자 입력 받기
user_input = st.text_input("Enter your query:")

# API 호출 함수 정의
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # 또는 사용할 다른 엔진
        prompt=prompt,
        max_tokens=150,  # 응답의 최대 토큰 수 설정
        n=1,  # 하나의 응답 생성
        stop=None,  # 지정된 토큰에서 멈춤
        temperature=0.7  # 응답의 창의성 조절 (0.0 ~ 1.0)
    )
    return response.choices[0].text.strip()

# 버튼 클릭 시 응답 표시
if st.button("Get Response"):
    if user_input:
        response = get_openai_response(user_input)
        st.text_area("Response:", response, height=200)
    else:
        st.warning("Please enter a query.")

# Streamlit 애플리케이션 실행
if __name__ == "__main__":
    st.write("OpenAI API Assistant Bot is ready to assist you!")
