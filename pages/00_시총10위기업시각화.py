import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 시가총액 상위 10개 기업
companies = {
    'Microsoft': 'MSFT',
    'Nvidia': 'NVDA',
    'Apple': 'AAPL',
    'Amazon': 'AMZN',
    'Alphabet (Google)': 'GOOGL',
    'Saudi Aramco': '2222.SR',  # 사우디 리야드 거래소
    'Meta Platforms': 'META',
    'Tesla': 'TSLA',
    'Berkshire Hathaway': 'BRK-B',  # 클래스 B 주식
    'Broadcom': 'AVGO'
}

# Yahoo Finance에서는 '-' 대신 '.' 사용해야 함 (예: BRK-B -> BRK.B)
adjusted_tickers = {name: ticker.replace('-', '.') for name, ticker in companies.items()}

# 데이터 다운로드 (최근 6개월)
df = yf.download(list(adjusted_tickers.values()), start="2024-11-01", end="2025-05-01")['Close']

# Plotly 그래프 생성
fig = go.Figure()

for name, ticker in adjusted_tickers.items():
    if ticker i
