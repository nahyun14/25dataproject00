import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("🌍 전 세계 환경 지도 - 탄소 배출량 시각화")
st.markdown("국가별 **이산화탄소(CO₂) 배출량**을 지도에 표시한 환경 정보 대시보드입니다.")

# 예시용 CO₂ 배출량 데이터 (실제로는 외부 CSV로 대체 가능)
data = {
    'Country': ['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Iran', 'South Korea', 'Saudi Arabia', 'Canada'],
    'CO2_emission': [10000, 5000, 2500, 1700, 1200, 900, 800, 700, 600, 550]
}
df = pd.DataFrame(data)

# 세계 지도 데이터 (geopandas의 내장 world 데이터)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# 국가명 기준 병합
world = world.merge(df, how='left', left_on='name', right_on='Country')

# Folium 지도 초기화
m = folium.Map(location=[20, 0], zoom_start=2)

# 색상 scale 설정
folium.Choropleth(
    geo_data=world,
    name="CO2 Emission",
    data=world,
    columns=["name", "CO2_emission"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="CO₂ 배출량 (Mt)",
    nan_fill_color="lightgray"
).add_to(m)

# 각 나라에 마커 추가
for idx, row in world.dropna(subset=['CO2_emission']).iterrows():
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=f"{row['name']}: {row['CO2_emission']} Mt",
        icon=folium.Icon(color='green', icon='leaf')
    ).add_to(m)

# 지도 보여주기
st_data = st_folium(m, width=1000, height=600)
