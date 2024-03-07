import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Jethro_Home",
        page_icon="🦊",
    )

    st.markdown(
        """
        Hello everybody, I am
        # Jethro Conde Lim
        #### **QA/SDET Engineer** \n
        This is a website to show mt cvs and works.
        """
    )


if __name__ == "__main__":
    run()
