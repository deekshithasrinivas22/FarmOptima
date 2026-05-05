# nav.py

import streamlit as st

def display_navbar(page_name="home"):
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Nunito:wght@300;400;600&display=swap');

    .block-container {
        padding-top: 0.8rem !important;
        padding-left: 8rem;
        padding-right: 3rem;
        max-width: 100%;
    }

    .stApp {
        background: #f5f4ef;
        font-family: 'Nunito', sans-serif;
    }

    header {
        visibility: hidden;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stSidebarNav"] {
        display: none;
    }

    .nav-title {
        font-size: 40px;
        font-family: 'Great Vibes', cursive;
        font-weight: 400;
        color: #2c3e28;
        margin-top: 8px;
    }

    div.stButton > button {
    background: transparent !important;
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
    color: #6f6658;
    font-size: 14px;
    font-weight: 600;
    margin-left: 0px;
    margin-top: 5px;
    padding: 0px;
    transition: 0.2s ease;
    white-space: nowrap;
    min-width: max-content;
}

div.stButton > button:hover {
    color: #3a5c38 !important;
    transform: translateY(-1px);
    border: none !important;
    box-shadow: none !important;
}

div.stButton > button:focus {
    outline: none !important;
    box-shadow: none !important;
    border: none !important;
}

div.stButton > button:active {
    outline: none !important;
    box-shadow: none !important;
    border: none !important;

}
    </style>
    """, unsafe_allow_html=True)

    nav1, nav2 = st.columns([6, 1.4])

    with nav1:
        st.markdown(
            "<div class='nav-title'>🍃 FarmOptima</div>",
            unsafe_allow_html=True
        )

    with nav2:
        b1, b2, b3 = st.columns([1.1, 1.6, 1.1])

        with b1:
            if st.button("Crops", key=f"nav_crop_{page_name}"):
                st.switch_page("pages/crop.py")

        with b2:
            if st.button("Irrigation", key=f"nav_irrigation_{page_name}"):
                st.switch_page("pages/irrigation.py")

        with b3:
            if st.button("Insights", key=f"nav_about_{page_name}"):
                st.switch_page("pages/about.py")

    st.markdown(
        "<hr style='border:2px solid #d7d4ca; margin-top:10px; margin-bottom:30px;'>",
        unsafe_allow_html=True
    )
