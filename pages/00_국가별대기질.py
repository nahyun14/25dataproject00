import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(layout="wide")
st.title("🌍 전 세계 대기질 지도")
st.markdown("전 세계 주요 도시의 **대기질 지수 (AQI)** 를 지도 위에 시각화한 환경 정보 대시보드입니다.")

# 확장된 AQI 데이터
data = [
    {"City": "Beijing", "Country": "China", "AQI": 180, "Lat": 39.9042, "Lon": 116.4074},
    {"City": "Delhi", "Country": "India", "AQI": 220, "Lat": 28.6139, "Lon": 77.2090},
    {"City": "Los Angeles", "Country": "USA", "AQI": 90, "Lat": 34.0522, "Lon": -118.2437},
    {"City": "London", "Country": "UK", "AQI": 60, "Lat": 51.5074, "Lon": -0.1278},
    {"City": "Seoul", "Country": "South Korea", "AQI": 110, "Lat": 37.5665, "Lon": 126.9780},
    {"City": "Paris", "Country": "France", "AQI": 70, "Lat": 48.8566, "Lon": 2.3522},
    {"City": "Moscow", "Country": "Russia", "AQI": 95, "Lat": 55.7558, "Lon": 37.6173},
    {"City": "Tokyo", "Country": "Japan", "AQI": 55, "Lat": 35.6895, "Lon": 139.6917},
    {"City": "Bangkok", "Country": "Thailand", "AQI": 130, "Lat": 13.7563, "Lon": 100.5018},
    {"City": "Cairo", "Country": "Egypt", "AQI": 160, "Lat": 30.0444, "Lon": 31.2357},
    {"City": "Mexico City", "Country": "Mexico", "AQI": 150, "Lat": 19.4326, "Lon": -99.1332},
    {"City": "Santiago", "Country": "Chile", "AQI": 140, "Lat": -33.4489, "Lon": -70.6693},
    {"City": "Jakarta", "Country": "Indonesia", "AQI": 200, "Lat": -6.2088, "Lon": 106.8456},
    {"City": "Tehran", "Country": "Iran", "AQI": 210, "Lat": 35.6892, "Lon": 51.3890},
    {"City": "Istanbul", "Country": "Turkey", "AQI": 125, "Lat": 41.0082, "Lon": 28.9784},
    {"City": "Lagos", "Country": "Nigeria", "AQI": 170, "Lat": 6.5244, "Lon": 3.3792},
    {"City": "Karachi", "Country": "Pakistan", "AQI": 190, "Lat": 24.8607, "Lon": 67.0011},
    {"City": "Buenos Aires", "Country": "Argentina", "AQI": 80, "Lat": -34.6037, "Lon": -58.3816},
    {"City": "Johannesburg", "Country": "South Africa", "AQI": 105, "Lat": -26.2041, "Lon": 28.0473},
    {"City": "New York", "Country": "USA", "AQI": 85, "Lat": 40.7128, "Lon": -74.0060},
]

df = pd.DataFrame(data)

# AQI에 따라 색상 반환
def get_color(aqi):
    if aqi <= 50:
        return "green"
    elif aqi <= 100:
        return "yellow"
    elif aqi <= 150:
        return "orange"
    elif aqi <= 200:
        return "red"
    elif aqi <= 300:
        return "purple"
    else:
        return "maroon"

# 지도 생성
m = folium.Map(location=[20, 0], zoom_start=2)

# 마커 추가
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Lat"], row["Lon"]],
        radius=10,
        color=get_color(row["AQI"]),
        fill=True,
        fill_opacity=0.7,
        popup=f"<b>{row['City']}, {row['Country']}</b><br>AQI: {row['AQI']}",
    ).add_to(m)

# 범례 HTML
legend_html = """
<div style='position: fixed; 
     bottom: 50px; left: 50px; width: 200px; height: 180px; 
     background-color: white; z-index:9999; font-size:14px;
     border:2px solid gray; padding: 10px;'>
<b>AQI 범례</b><br>
<span style='color:green;'>●</span> 0–50 (좋음)<br>
<span style='color:yellow;'>●</span> 51–100 (보통)<br>
<span style='color:orange;'>●</span> 101–150 (민감군 영향)<br>
<span style='color:red;'>●</span> 151–200 (나쁨)<br>
<span style='color:purple;'>●</span> 201–300 (매우 나쁨)<br>
<span style='color:maroon;'>●</span> 301+ (위험)
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# 스트림릿에 출력
st_data = st_folium(m, width=1000, height=600)
