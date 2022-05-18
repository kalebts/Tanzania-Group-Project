import streamlit as st
import plotly.express as px
from os.path import dirname, join, isfile
from os import listdir
from streamlit import components
from streamlit_folium import st_folium
import folium
import geopandas as gpd
import pandas as pd

st.set_page_config(layout="wide")

# water_service_df = pd.read_csv('tz_dataset') read sb's dataset


indicators = []

# help from https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
current_dir = dirname(__file__)
for file in listdir(current_dir):
    f = join(current_dir, file)
    if isfile(f) and 'tz_map' in file:
        indicators.append(file)
        
# tz_map_1_path = join(current_dir, "tz_map_1.html")
# tz_map_2_path = join(current_dir, "tz_map_2.html")

# template for maps: tz_map_(name_of_map).html
# then, split (name_of_map) by underscore.

st.title('Tanzania Water Pumps Analysis')

row1_1, row1_2 = st.columns((4, 5))


for i in range(len(indicators)):
    indicators[i] = " ".join(indicators[i][:-5].split('_')[2:])

indicators = tuple(indicators)

with row1_1:
    # indicator_button = st.selexctbox('Choose map', ('map 1', 'map 2'))
    indicator_button = st.selectbox('Choose indicator', indicators)


with row1_2:
    # components.v1.html(open(current_dir+'/tz_map_'+indicator_button+'.html').read(), height=600)
    streamlit_folium.st_folium