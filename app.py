import streamlit as st
import streamlit.components.v1 as components
from nav import display_navbar

st.set_page_config(
    page_title="FarmOptima",
    layout="wide",
    initial_sidebar_state="collapsed"
)

display_navbar()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&family=Nunito:wght@300;400;600&display=swap');

div.stButton > button[kind="primary"] {
    background: #4a7c42 !important;
    color: #f7f3ec !important;
    border: none !important;
    font-family: 'Nunito', sans-serif;
    font-size: 13px;
    font-weight: 600;
    padding: 11px 24px;
    border-radius: 100px;
    letter-spacing: 0.04em;
    box-shadow: none;
}

div.stButton > button[kind="secondary"] {
    background: transparent !important;
    color: #4a7c42 !important;
    border: none !important;
    font-family: 'Nunito', sans-serif;
    font-size: 13px;
    font-weight: 600;
    padding: 11px 24px;
    border-radius: 100px;
    letter-spacing: 0.04em;
    box-shadow: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)

left_margin, left, right, right_margin = st.columns([0.2, 1.2, 0.9, 0.2])

with left:
    components.html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600&family=Cormorant+Garamond:wght@300;400;500;600&display=swap');

    .hero-wrap {
        padding-top: 10px;
    }

    .hero-tag {
        display: inline-block;
        background: #e8f0e4;
        color: #3a5c38;
        font-size: 11px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        padding: 5px 14px;
        border-radius: 100px;
        margin-bottom: 1.2rem;
        font-weight: 600;
        font-family: 'Nunito', sans-serif;
    }

    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 58px;
        font-weight: 400;
        line-height: 0.92;
        letter-spacing: -0.05em;
        color: #223326;
        margin-bottom: 14px;
    }

    .hero-title em {
        color: #6e9b4d;
        font-style: italic;
        font-weight: 400;
    }

    .hero-body {
        font-size: 14px;
        color: #7a6e60;
        line-height: 1.9;
        font-weight: 300;
        max-width: 400px;
        font-family: 'Nunito', sans-serif;
        margin-bottom: 28px;
    }
    </style>

    <div class="hero-wrap">
        <div class="hero-tag">
            Smart Agriculture System
        </div>

        <div class="hero-title">
            Your farm,<br>
            <em>intelligently</em><br>
            guided
        </div>

        <div class="hero-body">
            AI recommendations for every decision — from which crop to plant,
            to exactly when to water. Built for farmers, explained in plain language.
        </div>
    </div>
    """, height=320)

    btn1, btn2, spacer = st.columns([1, 1.2, 3])

    with btn1:
        if st.button("Get started", key="hero_crop", type="primary"):
            st.switch_page("pages/crop.py")

    with btn2:
        if st.button("See how it works", key="hero_about"):
            st.switch_page("pages/about.py")

with right:
    top1, top2 = st.columns(2)
    bottom1, bottom2 = st.columns(2)

    with top1:
        st.markdown("""
        <div style="
            background:#3c5f3c;
            border-radius:20px;
            padding:30px;
            color:white;
            min-height:150px;
        ">
            <div style="font-size:42px;font-weight:700;">94%</div>
            <div style="margin-top:10px;color:#d7e5d7;">Crop accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with top2:
        st.markdown("""
        <div style="
            background:white;
            border-radius:20px;
            padding:30px;
            border:1px solid #e5e0d6;
            min-height:150px;
        ">
            <div style="font-size:42px;font-weight:700;color:#9b6a1f;">30%</div>
            <div style="margin-top:10px;color:#8c8170;">Water saved</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom1:
        st.markdown("""
        <div style="
            background:white;
            border-radius:20px;
            padding:30px;
            border:1px solid #e5e0d6;
            min-height:150px;
            margin-top:20px;
        ">
            <div style="font-size:42px;font-weight:700;color:#3c5f3c;">12</div>
            <div style="margin-top:10px;color:#8c8170;">Input features</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom2:
        st.markdown("""
        <div style="
            background:#f5ead6;
            border-radius:20px;
            padding:30px;
            min-height:150px;
            margin-top:20px;
        ">
            <div style="font-size:42px;font-weight:700;color:#9b6a1f;">3</div>
            <div style="margin-top:10px;color:#9b6a1f;">AI modules</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="
    margin-top:80px;
    margin-bottom:30px;
    font-size:14px;
    letter-spacing:0.25em;
    color:#b0a28f;
    font-weight:600;
">
    WHAT IT DOES
</div>
""", unsafe_allow_html=True)

card1, card2, card3 = st.columns(3)

with card1:
    components.html("""
    <div style="
        background:#fcfcfa;
        border:1px solid #d7e3cf;
        border-radius:30px;
        padding:40px 35px;
        min-height:420px;
        font-family:Nunito,sans-serif;
    ">
        <div style="
    width:68px;
    height:68px;
    border-radius:22px;
    background:#edf3e8;
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:30px;
    font-size:30px;
    color:#4e6c4a;
">
    ⟡
</div>

        <div style="
            font-size:14px;
            color:#c1b6a8;
            letter-spacing:0.2em;
            font-weight:600;
            margin-bottom:18px;
        ">
            01
        </div>

        <div style="
            font-family:'Cormorant Garamond', serif;
            font-size:32px;
            font-weight:600;
            color:#2f4030;
            margin-bottom:22px;
        ">
            Crop recommendation
        </div>

        <div style="
            font-size:17px;
            line-height: 1.2;
            color:#8f8374;
            margin-bottom:35px;
        ">
            Analyses soil composition, rainfall, and temperature to suggest the best crop for your land this season.
        </div>

        <div style="
            display:inline-block;
            background:#edf3e8;
            color:#4e6c4a;
            padding:10px 18px;
            border-radius:999px;
            font-size:13px;
            letter-spacing:0.12em;
            font-weight:600;
        ">
            RANDOM FOREST
        </div>
    </div>
    """, height=430)

with card2:
    components.html("""
    <div style="
        background:#fcfcfa;
        border:1px solid #e8ddcb;
        border-radius:30px;
        padding:40px 35px;
        min-height:420px;
        font-family:Nunito,sans-serif;
    ">
        <div style="
    width:68px;
    height:68px;
    border-radius:22px;
    background:#f4e8d4;
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:30px;
    font-size:30px;
    color:#9c6d1c;
">
    ◔
</div>

        <div style="
            font-size:14px;
            color:#c1b6a8;
            letter-spacing:0.2em;
            font-weight:600;
            margin-bottom:18px;
        ">
            02
        </div>

        <div style="
            font-family:'Cormorant Garamond', serif;
            font-size:32px;
            font-weight:600;
            color:#2f4030;
            margin-bottom:22px;
        ">
            Smart irrigation
        </div>

        <div style="
            font-size:17px;
            line-height:1.9;
            color:#8f8374;
            margin-bottom:35px;
        ">
            Fuses soil moisture readings with live weather to decide when and how much water your crops actually need.
        </div>

        <div style="
            display:inline-block;
            background:#f4e8d4;
            color:#9c6d1c;
            padding:10px 18px;
            border-radius:999px;
            font-size:13px;
            letter-spacing:0.12em;
            font-weight:600;
        ">
            SENSOR + WEATHER
        </div>
    </div>
    """, height=430)

with card3:
    components.html("""
    <div style="
        background:#fcfcfa;
        border:1px solid #d7e3df;
        border-radius:30px;
        padding:40px 35px;
        min-height:420px;
        font-family:Nunito,sans-serif;
    ">
        <div style="
    width:68px;
    height:68px;
    border-radius:22px;
    background:#e4f1ed;
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:30px;
    font-size:30px;
    color:#23856d;
">
    ◎
</div>

        <div style="
            font-size:14px;
            color:#c1b6a8;
            letter-spacing:0.2em;
            font-weight:600;
            margin-bottom:18px;
        ">
            03
        </div>

        <div style="
            font-family:'Cormorant Garamond', serif;
            font-size:32px;
            font-weight:600;
            color:#2f4030;
            margin-bottom:22px;
        ">
            Explainable AI
        </div>

        <div style="
            font-size:17px;
            line-height:1.9;
            color:#8f8374;
            margin-bottom:35px;
        ">
            Every recommendation comes with a plain-language breakdown of the factors that drove the decision.
        </div>

        <div style="
            display:inline-block;
            background:#e4f1ed;
            color:#23856d;
            padding:10px 18px;
            border-radius:999px;
            font-size:13px;
            letter-spacing:0.12em;
            font-weight:600;
        ">
            SHAP VALUES
        </div>
    </div>
    """, height=430)
