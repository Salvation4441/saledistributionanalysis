import streamlit as st
import pandas as pd
import plost
import os
from classes.data import total_sales_city, month_sales

st.set_page_config(layout='wide', initial_sidebar_state='expanded', )

# link css
css_path = os.path.join('static', 'style.css')
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


st.title(':blue[Dashboard]🏡')

# Card Display
st.markdown('###### Metrics')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Yearly Total Sales", "70 °F", "1.2 °F")
col2.metric("Quarterly Sales", "9 mph", "-8%")
col3.metric("Monthly Sales", "86%", "4%")
col4.metric("Weekly Sales", "9 mph", "-8%")

st.markdown('')
st.markdown('###### Line chart')
fig = total_sales_city()
st.plotly_chart(fig)
