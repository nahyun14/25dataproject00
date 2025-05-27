import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import date

st.set_page_config(page_title="글로벌 시총 10대 기업 주가 시각화", layout="wide")

# 🐱 타이틀
st.title("🌍 글로벌 시가총액 Top 10 기업 주가 추이")

st.markdown("""
이 앱은 Yahoo Finance 데이터를 기반으로 **2025년 기준 글로벌 시총 상위 10개 기업의 주가**를 시각화합니다.  
좌측의 필터를 통해 원하는 기업과 기간을 선택할 수 있어요! 📈
""")

# 🐾 시총 상위 10개 기업 정보
companies = {
    'Microsoft': 'MSFT',
    'Nvidia': 'NVDA',
    'Apple': 'AAPL',
    'Amazon': 'AMZN',
    'Alphabet (Google)': 'GOOGL',
    'Saudi Aramco': '2222.SR',
    'Meta Platforms': 'META',
    'Tesla': 'TSLA',
    'Berkshire Hathaway': 'BRK-B',
    'Broadcom': 'AVGO'
}

# 🐾 사이드바 필터
st.sidebar.header("📊 필터 선택")
selected_companies = st.sidebar.multiselect(
    "기업 선택",
    options=list(companies.keys()),
    default=list(companies.keys())
)

start_date = st.sidebar.date_input("시작 날짜", date(2024, 11, 1))
end_date = st.sidebar.date_input("종료 날짜", date(2025, 5, 1))

if start_date >= end_date:
    st.sidebar.error("종료 날짜는 시작 날짜보다 이후여야 합니다!")

# 🐾 선택된 기업의 티커 가져오기
selected_tickers = [companies[comp] for comp in selected_companies]

# 🐾 데이터 다운로드
@st.cache_data
def load_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)['Close']
    return data

if selected_tickers:
    with st.spinner("데이터 불러오는 중..."):
        df = load_data(selected_tickers, start_date, end_date)

    # 🐾 시각화
    fig = go.Figure()
    for ticker in selected_tickers:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df[ticker],
            mode='lines',
            name=ticker
        ))

    fig.update_layout(
        title="📈 주가 추이",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        template="plotly_white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("최소 한 개 이상의 기업을 선택해주세요!")
