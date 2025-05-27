import streamlit as st
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 🐾 타이틀
st.title("서울시 서초구 고등학교 지도")

# 🐾 고등학교 데이터 (동덕여고 포함!)
data = pd.DataFrame({
    '학교명': ['서울고등학교', '서초고등학교', '양재고등학교', '동덕여자고등학교'],
    '주소': [
        '서울 서초구 반포대로 45',
        '서울 서초구 서초중앙로 80',
        '서울 서초구 바우뫼로 118',
        '서울 서초구 반포대로 89'
    ],
    '위도': [37.499, 37.4925, 37.4786, 37.504768],
    '경도': [127.011, 127.015, 127.038, 127.009536]
})

# 🐾 지도 중심 좌표 (서초구 중심)
center_lat = 37.4836
center_lon = 127.0326

# 🐾 Folium 지도 생성
m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# 🐾 각 고등학교에 마커 추가
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['학교명'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# 🐾 지도 보여주기
st_folium(m, width=700, height=500)
