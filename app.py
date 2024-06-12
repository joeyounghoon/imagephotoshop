import streamlit as st

# HTML을 사용하여 이미지와 버튼을 함께 생성
button_html = """
    <style>
    .button-container {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .button-with-image {
        background-color: transparent;
        border: none;
        cursor: pointer;
        outline: none;
    }
    </style>
    <div class="button-container">
        <form action="?action=button_click" method="POST">
            <button class="button-with-image" type="submit">
                <img src="https://path-to-your-image.jpg" alt="Button Image" width="100" height="100">
            </button>
        </form>
    </div>
"""

# HTML을 사용하여 버튼을 렌더링
st.markdown(button_html, unsafe_allow_html=True)

# 버튼 클릭 시 처리할 작업
if st.experimental_get_query_params().get('action') == ['button_click']:
    st.write("Button clicked!")
