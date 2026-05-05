import streamlit as st
import streamlit.components.v1 as components
from nav import display_navbar

st.set_page_config(
    page_title="FarmOptima - About",
    layout="wide",
    initial_sidebar_state="collapsed"
)

display_navbar("about")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&family=Nunito:wght@300;400;600&display=swap');

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

.section-label {
    font-size: 12px;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: #b0a28f;
    font-weight: 600;
    margin-bottom: 1.5rem;
    margin-top: 2rem;
}

.metric-card {
    background: #fcfcfa;
    border: 1px solid #e5dfd2;
    border-radius: 28px;
    padding: 30px;
    min-height: 180px;
    margin-bottom: 20px;
}

.metric-label {
    font-size: 12px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #b0a28f;
    margin-bottom: 12px;
}

.metric-value {
    font-family: 'Cormorant Garamond', serif;
    font-size: 42px;
    color: #2f4030;
    font-weight: 600;
}

.metric-sub {
    margin-top: 10px;
    color: #8c8170;
    font-size: 14px;
    line-height: 1.7;
}

.info-card {
    background: rgba(252, 252, 250, 0.85);
    border: 1px solid #ddd2c4;
    border-radius: 28px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
}

.info-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 34px;
    color: #2f4030;
    margin-bottom: 1rem;
}

.info-text {
    color: #5d564d;
    font-size: 15px;
    line-height: 1.9;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 1.5rem;
}

.feature-card {
    background: rgba(247, 243, 236, 0.78);
    border: 1px solid #ddd2c4;
    border-radius: 20px;
    padding: 1.4rem;
}

.feature-title {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: #8f7d67;
    margin-bottom: 0.7rem;
    font-weight: 700;
}

.feature-text {
    color: #5d564d;
    font-size: 14px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1.4, 1])

with left:
    components.html("""
    <div style="padding-top:20px; font-family: Nunito, sans-serif;">
        <div style="display:inline-block;background:#e8f0e4;color:#3a5c38;font-size:11px;letter-spacing:0.18em;text-transform:uppercase;padding:6px 14px;border-radius:999px;margin-bottom:1.2rem;font-weight:600;">
            About FarmOptima
        </div>

        <div style="font-family:'Cormorant Garamond', serif;font-size:60px;font-weight:400;line-height:0.92;letter-spacing:-0.05em;color:#223326;margin-bottom:18px;">
            Helping farmers make<br>
            smarter decisions with<br>
            <span style="color:#6e9b4d;font-style:italic;">AI-powered agriculture</span>
        </div>

        <div style="font-size:15px;color:#7a6e60;line-height:1.9;font-weight:300;max-width:580px;">
            FarmOptima is designed to help farmers choose the best crops, improve irrigation planning,
            understand environmental conditions and make data-driven decisions for better productivity.
        </div>
    </div>
    """, height=420)

with right:
    components.html("""
    <div style="display:flex; flex-direction:column; gap:18px; padding-top:20px;">

        <div style="
            background:#3c5f3c;
            border-radius:30px;
            padding:30px;
            color:white;
            min-height:150px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">
            <div style="
                font-size:11px;
                letter-spacing:0.18em;
                text-transform:uppercase;
                opacity:0.8;
                margin-bottom:12px;
            ">
                FarmOptima
            </div>

            <div style="
                font-family:'Cormorant Garamond', serif;
                font-size:42px;
                line-height:1;
                margin-bottom:10px;
            ">
                Smarter Farming
            </div>

            <div style="
                font-size:14px;
                line-height:1.8;
                color:#d7e5d7;
                max-width:300px;
            ">
                Helping farmers make better crop and irrigation decisions using AI.
            </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">

            <div style="
                background:#fcfcfa;
                border:1px solid #e5dfd2;
                border-radius:24px;
                padding:24px;
                min-height:140px;
            ">
                <div style="
                    font-size:11px;
                    letter-spacing:0.14em;
                    text-transform:uppercase;
                    color:#a08f79;
                    margin-bottom:10px;
                ">
                    States Supported
                </div>

                <div style="
                    font-family:'Cormorant Garamond', serif;
                    font-size:42px;
                    color:#2f4030;
                ">
                    13
                </div>

                <div style="
                    font-size:14px;
                    color:#7d7264;
                    line-height:1.7;
                    margin-top:8px;
                ">
                    Indian states currently included in the project.
                </div>
            </div>

            <div style="
                background:#f5ead6;
                border-radius:24px;
                padding:24px;
                min-height:140px;
            ">
                <div style="
                    font-size:11px;
                    letter-spacing:0.14em;
                    text-transform:uppercase;
                    color:#9b6a1f;
                    margin-bottom:10px;
                ">
                    Focus Areas
                </div>

                <div style="
                    font-size:15px;
                    color:#8f6b24;
                    line-height:2;
                    font-weight:600;
                ">
                    Crop Planning<br>
                    Smart Irrigation<br>
                    Sustainable Farming
                </div>
            </div>
        </div>
    </div>
    """, height=420)
st.markdown("<div class='section-label'>Project Overview</div>", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <div class="info-title">What is FarmOptima?</div>
    <div class="info-text">
        FarmOptima is an agriculture-focused platform that helps farmers and agricultural planners make
        smarter choices using data and AI. The project focuses on improving productivity, reducing water waste,
        supporting crop selection and making farming decisions more efficient.
        <br><br>
        The platform combines seasonal information, weather conditions, rainfall estimates and crop requirements
        to provide practical recommendations that can support everyday farming activities.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-label'>Key Features</div>", unsafe_allow_html=True)

components.html("""
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; font-family:Nunito, sans-serif;">

    <div style="background:rgba(247,243,236,0.78); border:1px solid #ddd2c4; border-radius:20px; padding:22px;">
        <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.14em; color:#8f7d67; margin-bottom:10px; font-weight:700;">
            Crop Recommendation
        </div>
        <div style="color:#5d564d; font-size:14px; line-height:1.8;">
            Suggests the most suitable crop based on the selected state, season and soil-related conditions.
        </div>
    </div>

    <div style="background:rgba(247,243,236,0.78); border:1px solid #ddd2c4; border-radius:20px; padding:22px;">
        <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.14em; color:#8f7d67; margin-bottom:10px; font-weight:700;">
            Smart Irrigation
        </div>
        <div style="color:#5d564d; font-size:14px; line-height:1.8;">
            Calculates irrigation requirements using rainfall, temperature, crop type and land area.
        </div>
    </div>

    <div style="background:rgba(247,243,236,0.78); border:1px solid #ddd2c4; border-radius:20px; padding:22px;">
        <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.14em; color:#8f7d67; margin-bottom:10px; font-weight:700;">
            Weather Awareness
        </div>
        <div style="color:#5d564d; font-size:14px; line-height:1.8;">
            Uses estimated temperature and rainfall data to understand how environmental conditions affect farming.
        </div>
    </div>

    <div style="background:rgba(247,243,236,0.78); border:1px solid #ddd2c4; border-radius:20px; padding:22px;">
        <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.14em; color:#8f7d67; margin-bottom:10px; font-weight:700;">
            Sustainable Farming
        </div>
        <div style="color:#5d564d; font-size:14px; line-height:1.8;">
            Encourages better water management and more efficient agricultural planning.
        </div>
    </div>

</div>
""", height=320)

st.markdown("<div class='section-label'>Why This Project Matters</div>", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <div class="info-title">Building Better Farming Decisions</div>
    <div class="info-text">
        Agriculture depends heavily on climate, soil and water availability. Farmers often face uncertainty
        regarding which crops to grow and how much water to use.
        <br><br>
        FarmOptima aims to reduce this uncertainty by offering clear recommendations that are simple,
        visually understandable and easy to use. The project is especially useful for demonstrating how
        AI and data can be applied to real-world agricultural problems.
    </div>
</div>
""", unsafe_allow_html=True)
