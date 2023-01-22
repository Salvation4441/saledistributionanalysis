import os
import pandas as pd
import plotly.express as px
import streamlit as st

pd.options.display.float_format = '{:,.2f}'.format

# reading csv file
path = os.path.join('classes', 'ProcessedData.csv')

# print('%%%%%%%%%%%%%%% preparing to read %%%%%%%%%%%%%%%%')
data = pd.read_csv(path, encoding='latin1')


# get total sales of each city
@st.cache(suppress_st_warning=True)
def total_sales_city():
    fig = px.bar(
        data, x='City', y='Total_Sales', color='City',
        title='Total Sales for 4 Year',
        labels={'Total_Sales': 'Sales'},
        width=1100
    )
    return fig


@st.cache(suppress_st_warning=True, show_spinner=True)
def quarter_sales():
    fig = px.bar(data,
                 x='Order_Quarter',
                 y='Total_Sales',
                 color='Order_Quarter',
                 title='Quarter Sales for Each Year',
                 labels={'Order_Quarter': 'Order Quarter', 'Total_Sales': 'Sales'},
                 width=1100
                 )
    return fig


@st.cache(suppress_st_warning=True)
def month_sales():
    fig = px.bar(data,
                 x='Order_Month_Name',
                 y='Total_Sales',
                 color='Order_Year',
                 title='Total Sales for each month per year sorted based on months',
                 labels={'Order_Month_Name': 'Month Name', 'Total_Sales': 'Sales', 'Order_Year': 'Year'},
                 width=1100
                 )
    return fig
