import streamlit as st
import os

css_path = os.path.join('static', 'style.css')
# link css
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.title('Contact')
