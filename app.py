from openai import OpenAI
import streamlit as st

def get_openai_response(api_key, messages):
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key)
    
    # 응답 생성
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,  # 응답의 최대 토큰 수 설정
        temperature=0.7  # 응답의 창의성 조절 (0.0 ~ 1.0)
    )
    
    # 응답 텍스트 반환
    return response.choices[0].message['content'].strip()

# Streamlit 애플리케이션 설정
st.title("OpenAI API Assistant Bot")

# 사용자로부터 API 키 입력 받기
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# 초기 메시지 설정
initial_messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# 이전 메시지와 사용자 입력을 포함한 전체 메시지 리스트
messages = initial_messages

# 사용자 입력 받기
user_input = st.text_input("Enter your query:")

# 버튼 클릭 시 응답 표시
if st.button("Get Response"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not user_input:
        st.warning("Please enter a query.")
    else:
        # 사용자 입력을 메시지 리스트에 추가
        messages.append({"role": "user", "content": user_input})
        try:
            # OpenAI 응답 받기
            response = get_openai_response(api_key, messages)
            messages.append({"role": "assistant", "content": response})
            st.text_area("Response:", response, height=200)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Streamlit 애플리케이션 실행
if __name__ == "__main__":
    st.write("OpenAI API Assistant Bot is ready to assist you!")
