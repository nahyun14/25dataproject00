
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 시총 상위 10개 기업 티커
tickers = ['MSFT', 'NVDA', 'AAPL', 'AMZN', 'GOOGL', '2222.SR', 'META', 'TSLA', 'BRK-B', 'AVGO']

# 데이터 다운로드
data = yf.download(tickers, start="2024-11-01", end="2025-05-01")['Close']

# Plotly 그래프 생성
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
