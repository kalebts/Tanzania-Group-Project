import streamlit as st
import plotly.express as px
from os.path import dirname, join
from streamlit import components
import geopandas as gpd

current_dir = dirname(__file__)
tz_map_1_path = join(current_dir, "tz_map_1.html")
tz_map_2_path = join(current_dir, "tz_map_2.html")

st.set_page_config(layout="wide")

st.title('Tanzania Water Pumps Analysis')
st.header("Click the button to change between maps")
map_button = st.selectbox('Choose map', ('map 1', 'map 2'))

if map_button == 'map 1':
    components.v1.html(open(tz_map_1_path).read(), height=500)
elif map_button == 'map 2':
    components.v1.html((open(tz_map_2_path).read()), height=500)