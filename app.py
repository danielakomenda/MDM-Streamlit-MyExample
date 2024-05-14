import streamlit as st
import pymongo
import pandas as pd

st.set_page_config(page_title="Temperature")
st.header("Weather-Data")

# Initialize connection.
db_name = "MDM-Python-MeinProjekt"
collection_name = "Wetter_Durchschnitt"

@st.cache_resource
def init_connection():
    connection_uri = st.secrets["mongo"]["db_connectionstring"]
    return pymongo.MongoClient(connection_uri)

client = init_connection()

@st.cache_data(ttl=600)
def get_data():
    db = client[db_name]
    collection = db[collection_name]
    items = list(collection.find())
    return items

data = pd.DataFrame(get_data())
st.write("Raw data:")
st.write(data)

# Checkbox
show_avg_temp = st.checkbox("Show Average Temperature", value=True)
show_min_temp = st.checkbox("Show Min Temperature", value=True)
show_max_temp = st.checkbox("Show Max Temperature", value=True)

# Plots
if show_avg_temp:
    st.write("Average Temperature:")
    st.line_chart(data[['date', 'avg_temp']].set_index('date'), use_container_width=True, color="#8F00FF")
if show_min_temp:
    st.write("Minimal Temperature:")
    st.line_chart(data[['date', 'min_temp']].set_index('date'), use_container_width=True, color="#0000FF")
if show_max_temp:
    st.write("Maximal Temperature:")
    st.line_chart(data[['date', 'max_temp']].set_index('date'), use_container_width=True, color="#FF0000")

