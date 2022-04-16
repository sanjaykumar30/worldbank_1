import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.title("World Bank Data - India")
 

data=pd.read_csv("World_Bank_India.csv",skiprows=4)
data.set_index('Indicator Name',inplace=True)
data=data[['2010','2011','2012','2013','2014','2015','2016','2017','2018']]
data=data.transpose()
data=data[['Physicians (per 1,000 people)','Number of deaths ages 5-9 years','People using safely managed sanitation services, rural ({} of rural population)'.format('%')]]
st.table(data)
