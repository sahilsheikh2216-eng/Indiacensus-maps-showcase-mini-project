import streamlit as st

import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
df = pd.read_csv('/Users/sahil/PycharmProject/India_census_maps/india.csv')

list_of_state = list(df['State'].unique())
list_of_state.insert(0 , 'overall india')

st.sidebar.title('India ka data viz')

selected_state = st.sidebar.selectbox('select a State', list_of_state)
primary = st.sidebar.selectbox('select a Primary parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('select a secondary parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('plot graph')

if plot:
    st.text('size represent primary')
    st.text('color represents secondary parameter')
    if selected_state == 'overall india':
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                             color_continuous_scale=px.colors.cyclical.IceFire, zoom=3 ,width = 1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                             color_continuous_scale=px.colors.cyclical.IceFire,width = 1200, height=700,  zoom=3 , hover_name='District')

        st.plotly_chart(fig , use_container_width=True)


