import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import tempfile

st.title('MP3 파일 음성 분석')

# 파일 업로드
uploaded_file = st.file_uploader("MP3 또는 MP4 파일을 업로드하세요", type=["mp3", "mp4"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    # 파일을 임시 파일로 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    if file_extension == 'mp4':
        # MP4 파일을 MP3로 변환
        audio = AudioSegment.from_file(temp_file_path, format="mp4")
        mp3_temp_file_path = temp_file_path.replace('.mp4', '.mp3')
        audio.export(mp3_temp_file_path, format="mp3")
        temp_file_path = mp3_temp_file_path

    # librosa를 사용하여 오디오 파일 읽기
    y, sr = librosa.load(temp_file_path, sr=None)
    
    # 시간에 따른 파형 그리기
    st.header('파형')
    fig, ax = plt.subplots()
    librosa.display.waveshow(y, sr=sr, ax=ax)
    plt.xlabel('시간 (s)')
    plt.ylabel('진폭')
    st.pyplot(fig)
    
    # 시간에 따른 음성 주파수 스펙트로그램 그리기
    st.header('스펙트로그램')
    fig, ax = plt.subplots()
    S = librosa.feature.melspectrogram(y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', ax=ax)
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    plt.xlabel('시간 (s)')
    plt.ylabel('주파수 (Hz)')
    st.pyplot(fig)
    
    # 시간에 따른 음성 주파수 특징 추출 및 시각화
    st.header('주파수 특징')
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(chroma_stft, y_axis='chroma', x_axis='time', ax=ax)
    fig.colorbar(img, ax=ax)
    plt.xlabel('시간 (s)')
    plt.ylabel('주파수 (Hz)')
    st.pyplot(fig)
