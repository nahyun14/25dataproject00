import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import requests

st.set_page_config(layout="wide")
st.title("🌍 전 세계 환경 지도 - 탄소 배출량 시각화")
st.markdown("국가별 **이산화탄소(CO₂) 배출량**을 지도에 표시한 환경 정보 대시보드입니다.")

# 예시용 CO₂ 배출량 데이터
data = {
    'Country': ['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Iran', 'South Korea', 'Saudi Arabia', 'Canada'],
    'CO2_emission': [10000, 5000, 2500, 1700, 1200, 900, 800, 700, 600, 550]
}
df = pd.DataFrame(data)

# 세계 지도 GeoJSON 로딩
@st.cache_data
def load_geojson():
    url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
    response = requests.get(url)
    return response.json()

geojson_data = load_geojson()

# 지도 초기화
m = folium.Map(location=[20, 0], zoom_start=2)

# Choropleth 계층 추가
folium.Choropleth(
    geo_data=geojson_data,
    data=df,
    columns=["Country", "CO2_emission"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color="lightgray",
    legend_name="CO₂ 배출량 (Mt)"
).add_to(m)

# 마커 추가 (대표적인 위치만 수동 지정)
coordinates = {
    "China": [35.8617, 104.1954],
    "United States": [37.0902, -95.7129],
    "India": [20.5937, 78.9629],
    "Russia": [61.5240, 105.3188],
    "Japan": [36.2048, 138.2529],
    "Germany": [51.1657, 10.4515],
    "Iran": [32.4279, 53.6880],
    "South Korea": [35.9078, 127.7669],
    "Saudi Arabia": [23.8859, 45.0792],
    "Canada": [56.1304, -106.3468]
}

for _, row in df.iterrows():
    country = row["Country"]
    if country in coordinates:
        folium.Marker(
            location=coordinates[country],
            popup=f"{country}: {row['CO2_emission']} Mt",
            icon=folium.Icon(color='green', icon='leaf')
        ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=1000, height=600)
