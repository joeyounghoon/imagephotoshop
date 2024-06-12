pip install beautifulsoup4

import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

# op.gg에서 바텀 챔피언 상성 데이터 가져오기
def get_opgg_bottom_data(champion_name):
    url = f'https://www.op.gg/champion/{champion_name}/statistics/bot'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 바텀 챔피언 상성 데이터를 추출합니다.
    counter_champs = soup.find_all('div', class_='champion-stats-header-matchup__table--champion')
    win_rate = soup.find_all('div', class_='champion-stats-header-matchup__table--value')
    
    matchups = []
    for champ, rate in zip(counter_champs, win_rate):
        champ_name = champ.get_text(strip=True)
        win_rate = rate.get_text(strip=True)
        matchups.append(f'{champ_name}: {win_rate}')
    
    return matchups

# GPT-4 모델을 통해 바텀 상성 분석
def analyze_bottom_matchups(matchups):
    matchup_text = '\n'.join(matchups)
    prompt = f"Analyze the following bottom lane matchups and provide insights:\n{matchup_text}"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit 애플리케이션
st.title('OP.GG Bottom Lane Matchup Analysis with GPT-4')

champion_name = st.text_input('Enter Champion Name:')
if champion_name:
    matchups = get_opgg_bottom_data(champion_name)
    st.write(f'Bottom Lane Matchups for {champion_name}:')
    
    for matchup in matchups:
        st.write(matchup)
    
    analysis = analyze_bottom_matchups(matchups)
    st.write(f'Analysis by GPT-4:\n{analysis}')
