import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.title("World Bank Data - India")
data=pd.read_csv("World_Bank_India.csv",skiprows=4)
# sdata.set_index("Day",inplace=True)
st.write(data)
data['1960'][0]