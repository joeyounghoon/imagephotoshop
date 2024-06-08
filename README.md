# imagephotoshop
# AI Photoshop Web App

이 프로젝트는 사용자가 이미지를 업로드하고 편집 지침을 입력하면, OpenAI의 GPT-4를 사용하여 지침을 생성하고 Pillow를 사용하여 이미지를 편집하는 웹 애플리케이션입니다.

## 설치 방법

1. 이 저장소를 클론합니다:
    ```bash
    git clone https://github.com/your-username/ai-photoshop-web-app.git
    cd ai-photoshop-web-app
    ```

2. 가상 환경을 설정하고 활성화합니다:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows에서는 `venv\Scripts\activate`
    ```

3. 필요한 패키지를 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```

4. `app.py`를 실행합니다:
    ```bash
    streamlit run app.py
    ```

## 사용 방법

1. OpenAI API 키를 준비합니다.
2. 이미지를 업로드하고 편집 지침을 입력한 후, OpenAI API 키를 입력합니다.
3. '원본 이미지'와 '편집된 이미지'를 확인합니다.

## 기여

기여는 언제나 환영입니다! 개선 사항이나 버그 수정을 위한 Pull Request를 보내주세요.
