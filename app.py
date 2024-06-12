import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_opgg_data(summoner_name):
    url = f'https://www.op.gg/summoners/kr/%EC%A4%91%EC%84%B1%EB%A7%88%EB%85%80%20%EC%A3%A0%EB%A7%88-KR1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 필요한 데이터를 추출하는 로직을 여기에 작성합니다.
    # 예: 최근 경기 데이터, KDA, 승률 등
    # 이 예제에서는 간단히 페이지 제목을 추출합니다.
    title = soup.title.string
    
    return title

st.title('OP.GG Summoner Lookup')

summoner_name = st.text_input('Enter Summoner Name:')
if summoner_name:
    data = get_opgg_data(summoner_name)
    st.write(f'Data for {summoner_name}: {data}')
