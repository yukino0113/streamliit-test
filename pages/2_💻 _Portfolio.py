import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def portfolio():
    st.set_page_config(
        page_title="Jethro_Porfolio",
        page_icon="🦊",
    )


portfolio()