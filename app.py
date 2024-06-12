import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

st.title('MP3 파일 음성 분석')

# 파일 업로드
uploaded_file = st.file_uploader("MP3 파일을 업로드하세요", type=["mp3"])

if uploaded_file is not None:
    # librosa를 사용하여 오디오 파일 읽기
    y, sr = librosa.load(uploaded_file, sr=None)
    
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
