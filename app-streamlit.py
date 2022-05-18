from re import X
import streamlit as st
import plotly.express as px
from os.path import dirname, join, isfile
from os import listdir
from streamlit import components
from streamlit_folium import st_folium
import plost
import folium
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as cx
from shapely.geometry import Point

st.set_page_config(layout="wide") # make app wide

# read sb's dataset
sb_water_df = pd.read_csv('cleaned_data_sb/geo_func_precip_util_joined.csv')

# dataset with pump function status, for map and accompanying chart
st_functional_pumps = pd.read_csv('st_data/st_functional_pumps.csv').sort_values('Region')
st_functional_pumps.replace({'functional_need_repair': 'need repairs'}, inplace=True)
st_functional_pumps.replace({'non_functional': 'non functional'}, inplace=True)

# tz_regions geodataframe - for plotting static region maps
mixed_tz = gpd.read_file('mixed_tz/mixed_tz.shp')
mixed_tz.set_index('Region', inplace=True)

# ORIGINAL water pumps dataframe
water_pumps = pd.read_csv('./data/Pump_it_Up_Data_Mining_the_Water_Table_-_Training_set_values.csv')
water_pumps_targets = pd.read_csv('./data/Pump_it_Up_Data_Mining_the_Water_Table_-_Training_set_labels.csv')
water_pumps = pd.merge(left=water_pumps, right=water_pumps_targets, on='id', how='left')
water_pumps['geometry'] = [Point(xy) for xy in zip(water_pumps['longitude'], water_pumps['latitude'])] 
water_pumps.replace({'Dar es Salaam': 'Dar-es-salaam'}, inplace=True)

# sanitation data for line graphs
sanitation_data = pd.read_csv('st_data/sanitation_by_region.csv')

# drinking water quality data for line graphs
drinking_water_quality = pd.read_csv('st_data/drinking_water_quality_by_region.csv')

indicators_with_underscores = []

# help from https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
current_dir = dirname(__file__)
for file in listdir(current_dir + '/maps_kalebts/'):
    f = join(current_dir + '/maps_kalebts/', file)
    if isfile(f) and 'tz_map' in file:
        indicators_with_underscores.append(file)

# template for maps: tz_map_(name_of_map).html
# then, split (name_of_map) by underscore.

indicators = {}

for i in range(len(indicators_with_underscores)):
    button_name = indicators_with_underscores[i][:-5].split('_')[2:]

    button_name[0] = button_name[0].capitalize()

    for j in range(1, len(button_name)):
        if button_name[j] == 'percentage':
            button_name[j] = '(%)'

    indicators[" ".join(button_name)] = indicators_with_underscores[i]

page = st.sidebar.selectbox('Select page',
  ['Country','Region'])

st.title('🇹🇿 Tanzania Water Pumps App 🇹🇿')

st.markdown("""---""")

if (page=='Country'):
    indicator_button = st.selectbox('Choose indicator', tuple(indicators.keys()))
    
    components.v1.html(open(current_dir+'/maps_kalebts/'+indicators[indicator_button]).read(), height=600)

    st.text(' ')
    st.text(' ')
    st.text(' ')
    st.text(' ')

    if 'functional' in indicator_button.lower():
        st.vega_lite_chart(
            st_functional_pumps,
            {
                "title": "Percentages of Water Pump Status by Region",
                "width": {"step": 85},
                "height": 500,
                # 'orient': 'horizontal',
                "mark": "bar",
                "encoding": {
                    "x": {"field": "Region", 'type':'nominal'},
                    "y": {
                        "field": 'Percentage',
                        "aggregate": "sum",
                        # 'type': 'quantitative',
                        "stack":  "normalize"
                    },
                    "tooltip": {"field": "Percentage", "type": "quantitative"},
                    "color": {
                        "field": "Status",
                        "type": "ordinal",
                        "scale": {"range": ["#1EB53A", "#00A3DD", "#FCD116"]},
                        },
                    "opacity": {"value": 0.7},
                }
            }
        )
        
st.text(' ')
st.text(' ')
st.text(' ')
st.text(' ')

if (page=='Region'):
    row2_1, row2_2 = st.columns((5, 5))

    regions_choices = tuple(sb_water_df['Region_Nam'])

    with row2_1:
        region_button = st.selectbox('Choose region', tuple(regions_choices))
        region_indicator_button = st.selectbox('Choose region indicator', tuple(['None', 'Sanitation', 'Drinking Water Quality']))
        
        region_indicator_button=region_indicator_button

        st.text(" ")
        st.text(" ")

        if region_indicator_button=='None':
            st.empty()

        if region_indicator_button=='Sanitation':
            st.vega_lite_chart(
                sanitation_data[sanitation_data['Region'] == region_button],
                {
                    # "width": 900,
                    "transform":[
                        {"calculate": "2*datum.Type", "as": "b2"},
                    ],
                    "height": 500,
                    "background": "#5e5e5e",
                    "mark": {
                        "type": "line",
                        "point": "true",
                        "borders": {
                            "opacity": 0.5,
                            "strokeDash": [6, 4]
                        }
                    },
                    "encoding": {
                        "x": {"field": "Year"},
                        "y": {"field": "Percentage", "type": "quantitative"},
                        "strokeDash": {"field": "symbol", "type": "nominal"},
                        "axis": {
                            "tickCount": 5,
                        },
                        "tooltip": {"field": "Percentage", "type": "quantitative"},
                        "color": {
                            "field": "Type",
                            "type": "ordinal",
                            "scale": {"range": ["blue", "orange", "green", "red"]},
                        },
                    }
                }
            , use_container_width=True)

        if region_indicator_button=='Drinking Water Quality':
            st.vega_lite_chart(
                drinking_water_quality[drinking_water_quality['Region'] == region_button],
                {
                    "height": 500,
                    "background": "#5e5e5e",
                    "mark": {
                        "type": "line",
                        "point": "true",
                        "borders": {
                            "opacity": 0.5,
                            "strokeDash": [6, 4]
                        }
                    },
                    "encoding": {
                        "x": {"field": "Year"},
                        "y": {"field": "Percentage", "type": "quantitative"},
                        "strokeDash": {"field": "symbol", "type": "nominal"},
                        "axis": {
                            "tickCount": 5,
                        },
                        "tooltip": {"field": "Percentage", "type": "quantitative"},
                        "color": {
                            "field": "Type",
                            "type": "ordinal",
                            "scale": {"range": ["green", "blue", "orange", "red"]},
                            "sort": ["basic", "limited", "unimproved", "surface"],
                            # 'legend': {"values": ["Basic", "Limited", "Open Defecation", "Unimproved"]}
                        },
                    }
                }
            , use_container_width=True)

    with row2_2:
        region_plot = mixed_tz.loc[[region_button]].plot(
            figsize=(12,12), color='grey', alpha=0.075, legend=True,  edgecolor='black', linewidth=3, legend_kwds={'shrink': 0.3});

        cx.add_basemap(region_plot, source=cx.providers.Esri.WorldTopoMap, crs=mixed_tz.crs)

        gpd.GeoDataFrame(water_pumps[['source', 'status_group', 'geometry', 'region']][(water_pumps['region']==region_button) 
            & (water_pumps['status_group'] == 'functional')]).plot(ax=region_plot, marker='o', color='green', markersize=1);

        gpd.GeoDataFrame(water_pumps[['source', 'status_group', 'geometry', 'region']][(water_pumps['region']==region_button) 
            & (water_pumps['status_group'] == 'functional needs repair')]).plot(ax=region_plot, marker='o', color='blue', markersize=1);

        gpd.GeoDataFrame(water_pumps[['source', 'status_group', 'geometry', 'region']][(water_pumps['region']==region_button) 
            & (water_pumps['status_group'] == 'non functional')]).plot(ax=region_plot, marker='o', color='yellow', markersize=1);    
        

        st.pyplot(region_plot.figure, clear_figure=True)
