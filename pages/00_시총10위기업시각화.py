import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 🐾 1. 티커 목록
tickers = ['MSFT', 'NVDA', 'AAPL', 'AMZN', 'GOOGL', '2222.SR', 'META', 'TSLA', 'BRK-B', 'AVGO']

# 🐾 2. 데이터 다운로드 (최근 6개월)
data = yf.download(tickers, start="2024-11-01", end="2025-05-01")['Close']

# 🐾 3. Plotly 시각화
fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data[ticker],
        mode='lines',
        name=ticker
    ))

fig.update_layout(
    title='글로벌 시가총액 상위 10개 기업의 주가 추이 (2024.11 ~ 2025.05)',
    xaxis_title='날짜',
    yaxis_title='주가 (USD)',
    template='plotly_white',
    height=600
)

fig.show()
