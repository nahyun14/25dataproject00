import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(layout="wide")
st.title("🌍 전 세계 대기질 지도")
st.markdown("국가별 또는 주요 도시별 **대기질 지수 (AQI)** 를 시각화한 대시보드입니다.")

# 예시용 AQI 데이터
data = [
    {"City": "Beijing", "Country": "China", "AQI": 180, "Lat": 39.9042, "Lon": 116.4074},
    {"City": "Delhi", "Country": "India", "AQI": 220, "Lat": 28.6139, "Lon": 77.2090},
    {"City": "Los Angeles", "Country": "USA", "AQI": 90, "Lat": 34.0522, "Lon": -118.2437},
    {"City": "London", "Country": "UK", "AQI": 60, "Lat": 51.5074, "Lon": -0.1278},
    {"City": "Seoul", "Country": "South Korea", "AQI": 110, "Lat": 37.5665, "Lon": 126.9780},
    {"City": "Paris", "Country": "France", "AQI": 70, "Lat": 48.8566, "Lon": 2.3522},
    {"City": "Moscow", "Country": "Russia", "AQI": 95, "Lat": 55.7558, "Lon": 37.6173},
    {"City": "Tokyo", "Country": "Japan", "AQI": 55, "Lat": 35.6895, "Lon": 139.6917}
]

df = pd.DataFrame(data)

# 색상 매핑 함수
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

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Lat"], row["Lon"]],
        radius=10,
        color=get_color(row["AQI"]),
        fill=True,
        fill_opacity=0.7,
        popup=f"{row['City']}, {row['Country']}<br>AQI: {row['AQI']}"
    ).add_to(m)

# 범례 추가
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

# 지도 출력
st_data = st_folium(m, width=1000, height=600)
