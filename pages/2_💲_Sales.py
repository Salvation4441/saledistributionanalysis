import streamlit as st
import os

from classes.data import total_sales_city, quarter_sales, month_sales

css_path = os.path.join('static', 'style.css')
# link css
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.title(':blue[Sales]💲')

with st.expander("Sales Performance", expanded=True):
    tabs = ['Year Sales', 'Quarterly Sales', 'Monthly Sales Performance', 'Annual Sales Performance',
            '% Changes in Sales']

    tab1, tab2, tab3, tab4, tab5 = st.tabs(tabs)
    with tab1:
        st.write('December is the month with most sales as February is seen as the month with the least sales')
        # st.plotly_chart(total_sales_city())
        st.plotly_chart(quarter_sales())

    with tab2:
        st.markdown("""""")
        st.write('December is the month with most sales as February is seen as the month with the least sales')
        # st.plotly_chart(quarter_sales())

    with tab3:
        st.write('December is the month with most sales as February is seen as the month with the least sales')
        # st.plotly_chart(month_sales())

    with tab4:
        st.text('products_market_target()')

    with tab5:
        st.text('products_market_target()')
        # result, fig = 'percentage_changes(graph_type1)'
        # st.plotly_chart(fig)


