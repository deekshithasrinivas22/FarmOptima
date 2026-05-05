import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from nav import display_navbar
from textwrap import dedent

st.set_page_config(
    page_title="FarmOptima - Smart Irrigation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

display_navbar("irrigation")

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
    line-height: 1.6;
}

.reason-card {
    background: rgba(247, 243, 236, 0.78);
    border: 1px solid #ddd2c4;
    border-radius: 22px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

.reason-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: #9c8f7b;
    font-weight: 700;
    margin-bottom: 0.7rem;
}

.reason-text {
    color: #5d564d;
    font-size: 14px;
    line-height: 1.9;
}

.final-insight-card {
    background: rgba(229, 239, 227, 0.72);
    border: 1px solid #d7e2d4;
    border-radius: 24px;
    padding: 1.6rem 1.8rem;
    margin-top: 1.2rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.final-insight-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: #4a7c42;
    font-weight: 700;
    margin-bottom: 1rem;
}

.final-insight-text {
    color: #4e5d47;
    font-size: 14px;
    line-height: 2;
}

.result-card {
    background: rgba(252, 252, 250, 0.78);
    border: 1px solid #ddd2c4;
    border-radius: 28px;
    padding: 40px;
    margin-top: 20px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.result-pill {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 12px;
    letter-spacing: 0.12em;
    font-weight: 600;
    margin-bottom: 20px;
}

.result-status {
    font-family: 'Cormorant Garamond', serif;
    font-size: 44px;
    color: #2f4030;
    font-weight: 600;
    margin-bottom: 18px;
}

.result-text {
    color: #5d564d;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-testid="stButton"] > button[kind="primary"] {
    background: #4a7c42 !important;
    color: white !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 0.7rem 1.4rem !important;
    font-weight: 600 !important;
}

div[data-testid="stButton"] > button[kind="primary"]:hover {
    background: #3d6937 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_soil():
    try:
        df = pd.read_csv("dataset/Soil.csv")
        df.columns = df.columns.str.strip()
        df['State/UT'] = df['State/UT'].str.lower()
        return df
    except:
        st.error("Soil dataset not found. Check file path.")
        return pd.DataFrame()

soil_data = load_soil()

states = [
    "Karnataka", "Tamil Nadu", "Kerala", "Maharashtra",
    "Punjab", "Haryana", "Uttar Pradesh", "Rajasthan",
    "Gujarat", "West Bengal", "Bihar", "Odisha", "Madhya Pradesh"
]

seasons = ["Kharif", "Rabi", "Summer", "Winter", "Monsoon"]
crops = ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane"]

def weather(state, season):
    if state in ["Kerala", "West Bengal", "Odisha"]:
        temp, rain = 28, 150
    elif state in ["Rajasthan", "Gujarat"]:
        temp, rain = 36, 25
    else:
        temp, rain = 32, 70

    if season == "Summer":
        temp += 4
        rain -= 40
    elif season in ["Monsoon", "Kharif"]:
        rain += 80
    elif season == "Winter":
        temp -= 5

    rain = max(rain, 0)
    return temp, rain

left, right = st.columns([1.4, 1])

with left:
    components.html("""
    <div style="padding-top:20px; font-family: Nunito, sans-serif;">
        <div style="display:inline-block;background:#e8f0e4;color:#3a5c38;font-size:11px;letter-spacing:0.18em;text-transform:uppercase;padding:6px 14px;border-radius:999px;margin-bottom:1.2rem;font-weight:600;">
            Smart Irrigation System
        </div>

        <div style="font-family:'Cormorant Garamond', serif;font-size:60px;font-weight:400;line-height:0.92;letter-spacing:-0.05em;color:#223326;margin-bottom:18px;">
            Water your crops<br>
            with <span style="color:#6e9b4d;font-style:italic;">precision</span><br>
            and confidence
        </div>

        <div style="font-size:15px;color:#7a6e60;line-height:1.9;font-weight:300;max-width:560px;">
            Monitor rainfall, temperature, soil nutrients and crop needs
            to generate a smart irrigation recommendation for your land.
        </div>
    </div>
    """, height=420)

with right:
    top1, top2 = st.columns(2)
    bottom1, bottom2 = st.columns(2)

    with top1:
        st.markdown("""
        <div class="metric-card" style="background:#3c5f3c; border:none;">
            <div class="metric-label" style="color:#dbe8d8;">Water Saved</div>
            <div class="metric-value" style="color:white;">30%</div>
            <div class="metric-sub" style="color:#d7e5d7;">Less water waste</div>
        </div>
        """, unsafe_allow_html=True)

    with top2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Smart Factors</div>
            <div class="metric-value">4</div>
            <div class="metric-sub">Rainfall, crop, soil, temperature</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Coverage</div>
            <div class="metric-value">13</div>
            <div class="metric-sub">Supported Indian states</div>
        </div>
        """, unsafe_allow_html=True)

    with bottom2:
        st.markdown("""
        <div class="metric-card" style="background:#f5ead6; border:none;">
            <div class="metric-label" style="color:#9b6a1f;">Recommendation</div>
            <div class="metric-value" style="color:#9b6a1f;">AI</div>
            <div class="metric-sub" style="color:#9b6a1f;">Personalized irrigation logic</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div class='section-label'>Farm Details</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    state = st.selectbox("State", states)

with col2:
    season = st.selectbox("Season", seasons)

with col3:
    crop = st.selectbox("Crop", crops)

with col4:
    area = st.slider("Farm Area (acres)", 1, 500, 100)

temp, rain = weather(state, season)

st.markdown("<div class='section-label'>Weather Conditions</div>", unsafe_allow_html=True)

weather_col1, weather_col2 = st.columns(2)

with weather_col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Temperature</div>
        <div class="metric-value">{temp}°C</div>
        <div class="metric-sub">Based on selected state and season</div>
    </div>
    """, unsafe_allow_html=True)

with weather_col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Rainfall</div>
        <div class="metric-value">{rain} mm</div>
        <div class="metric-sub">Estimated seasonal rainfall</div>
    </div>
    """, unsafe_allow_html=True)



# PLACE THIS BELOW ALL YOUR IMPORTS AND AFTER YOU DEFINE temp, rain, crop etc.

# REPLACE EVERYTHING FROM:
# if st.button("💧 Check Irrigation", type="primary"):
# UNTIL THE END OF THE FILE

if st.button(
    "💧 Check Irrigation",
    type="primary",
    key="irrigation_button_main"
):

    reasons = []
    irrigation_score = 0

    if rain < 30:
        irrigation_score += 2
        reasons.append({
            "title": "Rainfall Analysis",
            "icon": "🌧️",
            "text": f"Rainfall is very low at {rain} mm, meaning the soil will not retain enough natural moisture for healthy crop growth.",
            "class": "red"
        })
    elif rain < 70:
        irrigation_score += 1
        reasons.append({
            "title": "Rainfall Analysis",
            "icon": "🌦️",
            "text": f"Rainfall is moderate at {rain} mm, so your crops may still need additional irrigation support.",
            "class": "yellow"
        })
    else:
        reasons.append({
            "title": "Rainfall Analysis",
            "icon": "💧",
            "text": f"Rainfall is sufficient at {rain} mm, providing strong natural moisture support for the soil.",
            "class": "green"
        })

    if temp > 35:
        irrigation_score += 2
        reasons.append({
            "title": "Temperature Impact",
            "icon": "☀️",
            "text": f"Temperature is very high at {temp}°C, causing faster evaporation and quicker moisture loss.",
            "class": "red"
        })
    elif temp > 30:
        irrigation_score += 1
        reasons.append({
            "title": "Temperature Impact",
            "icon": "🌤️",
            "text": f"Temperature is moderately warm at {temp}°C, which increases evaporation from the soil surface.",
            "class": "yellow"
        })
    else:
        reasons.append({
            "title": "Temperature Impact",
            "icon": "❄️",
            "text": f"Cooler temperature of {temp}°C helps preserve soil moisture for longer durations.",
            "class": "green"
        })

    crop_water_need = {
        "Rice": 3,
        "Sugarcane": 3,
        "Cotton": 2,
        "Maize": 2,
        "Wheat": 1
    }

    crop_explanations = {
        "Rice": "Rice requires a consistently wet environment and therefore needs high irrigation support.",
        "Sugarcane": "Sugarcane is a water-intensive crop grown over a long period of time.",
        "Cotton": "Cotton requires moderate irrigation during critical growth stages.",
        "Maize": "Maize performs best with balanced irrigation and controlled watering cycles.",
        "Wheat": "Wheat generally requires lower water input compared to most other crops."
    }

    irrigation_score += crop_water_need[crop]

    if crop_water_need[crop] == 3:
        crop_class = "red"
    elif crop_water_need[crop] == 2:
        crop_class = "yellow"
    else:
        crop_class = "green"

    reasons.append({
        "title": "Crop Water Requirement",
        "icon": "🌾",
        "text": crop_explanations[crop],
        "class": crop_class
    })

    if irrigation_score >= 6:
        status = "High Irrigation Needed"
        status_color = "#b8402a"
        pill_bg = "#f6ddd7"
        pill_text = "#a54434"
    elif irrigation_score >= 3:
        status = "Moderate Irrigation Needed"
        status_color = "#8f6b24"
        pill_bg = "#f4e8c9"
        pill_text = "#8a6a25"
    else:
        status = "Low Irrigation Needed"
        status_color = "#3f6f42"
        pill_bg = "#dcebd8"
        pill_text = "#456b48"

    st.markdown("""
<style>
.decision-heading {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: #a89b89;
    margin-top: 1.2rem;
    margin-bottom: 0.7rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid #d9d2c6;
    font-weight: 700;
}

.decision-card {
    border-radius: 18px;
    padding: 1.3rem;
    margin-bottom: 1rem;
    border-left: 5px solid;
}

.decision-card.green {
    background: rgba(229, 239, 227, 0.72);
    border-color: #4a7c42;
}

.decision-card.yellow {
    background: rgba(248, 239, 223, 0.72);
    border-color: #ba7517;
}

.decision-card.red {
    background: rgba(248, 227, 224, 0.72);
    border-color: #c84d3a;
}

.decision-top {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 0.7rem;
}

.decision-icon {
    font-size: 18px;
}

.decision-title {
    font-size: 20px;
    font-family: 'Cormorant Garamond', serif;
    color: #2f4030;
}

.decision-text {
    color: #5d564d;
    font-size: 14px;
    line-height: 1.8;
}

.final-result-card {
    background: rgba(252, 252, 250, 0.95);
    border: 1px solid #ddd2c4;
    border-radius: 28px;
    padding: 2rem;
    margin-top: 2rem;
}

.result-pill {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 11px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 1.2rem;
}

.result-heading {
    font-family: 'Cormorant Garamond', serif;
    font-size: 48px;
    color: #2f4030;
    margin-bottom: 1rem;
}

.result-description {
    color: #5d564d;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 2rem;
}

.insight-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 1rem;
}

.insight-box {
    background: rgba(247, 243, 236, 0.78);
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.2rem;
}

.insight-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #9c8f7b;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

.insight-value {
    font-size: 15px;
    color: #2f4030;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

    if irrigation_score >= 6:
        water_requirement = "High"
        frequency = "Daily or every 1–2 days"
        water_estimate = area * 1200
    elif irrigation_score >= 3:
        water_requirement = "Moderate"
        frequency = "Every 2–3 days"
        water_estimate = area * 750
    else:
        water_requirement = "Low"
        frequency = "Twice per week"
        water_estimate = area * 400

    st.markdown("<div class='decision-heading'>Irrigation Summary</div>", unsafe_allow_html=True)

    summary_html = f"""
<style>
.final-result-card {{
    background: rgba(252, 252, 250, 0.95);
    border: 1px solid #ddd2c4;
    border-radius: 28px;
    padding: 2rem;
    margin-top: 2rem;
    font-family: 'Nunito', sans-serif;
}}

.result-pill {{
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 11px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 1.2rem;
}}

.result-heading {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 42px;
    color: #2f4030;
    margin-bottom: 1rem;
}}

.result-description {{
    color: #5d564d;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 2rem;
}}

.insight-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}}

.insight-box {{
    background: rgba(247, 243, 236, 0.78);
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.2rem;
}}

.insight-label {{
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #9c8f7b;
    margin-bottom: 0.5rem;
    font-weight: 700;
}}

.insight-value {{
    font-size: 15px;
    color: #2f4030;
    line-height: 1.8;
}}
</style>

<div class="final-result-card">
    <div class="result-pill" style="background:{pill_bg}; color:{pill_text};">
        Smart Irrigation Recommendation
    </div>

    <div class="result-heading">
        {status}
    </div>

    <div class="result-description">
        Based on rainfall, temperature and crop water demand, your land currently falls under a
        <span style="color:{status_color}; font-weight:600;">
            {status.lower()}
        </span> category.
    </div>

    <div class="insight-grid">
        <div class="insight-box">
            <div class="insight-label">Water Requirement</div>
            <div class="insight-value">{water_requirement}</div>
        </div>

        <div class="insight-box">
            <div class="insight-label">Suggested Frequency</div>
            <div class="insight-value">{frequency}</div>
        </div>

        <div class="insight-box">
            <div class="insight-label">Irrigation Score</div>
            <div class="insight-value">{irrigation_score} / 8</div>
        </div>

        <div class="insight-box">
            <div class="insight-label">Estimated Water Required</div>
            <div class="insight-value">{water_estimate:,} litres for {area} acres</div>
        </div>
    </div>
</div>
"""

    components.html(summary_html, height=520)
    st.markdown("<div class='decision-heading'>Detailed Decision Breakdown</div>", unsafe_allow_html=True)

    for reason in reasons:
        st.markdown(f"""
        <div class="decision-card {reason['class']}">
            <div class="decision-top">
                <div class="decision-icon">{reason['icon']}</div>
                <div class="decision-title">{reason['title']}</div>
            </div>
            <div class="decision-text">
                {reason['text']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    final_insight_html = f"""
    <style>
    .final-result-card {{
        background: rgba(252, 252, 250, 0.95);
        border: 1px solid #ddd2c4;
        border-radius: 28px;
        padding: 2rem;
        margin-top: 1rem;
        font-family: 'Nunito', sans-serif;
    }}

    .result-pill {{
        display: inline-block;
        padding: 10px 18px;
        border-radius: 999px;
        font-size: 11px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 1.2rem;
    }}

    .insight-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }}

    .insight-box {{
        background: rgba(247, 243, 236, 0.78);
        border: 1px solid #ddd2c4;
        border-radius: 18px;
        padding: 1.2rem;
    }}

    .insight-label {{
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #9c8f7b;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }}

    .insight-value {{
        font-size: 15px;
        color: #2f4030;
        line-height: 1.8;
    }}
    </style>

    <div class="final-result-card">
        <div class="result-pill" style="background:{pill_bg}; color:{pill_text};">
            Final Insight
        </div>

        <div class="insight-grid">
            <div class="insight-box">
                <div class="insight-label">Rainfall Condition</div>
                <div class="insight-value">
                    {"Low rainfall detected" if rain < 30 else "Moderate rainfall detected" if rain < 70 else "Good rainfall detected"}
                </div>
            </div>

            <div class="insight-box">
                <div class="insight-label">Temperature Condition</div>
                <div class="insight-value">
                    {"High temperature causing moisture loss" if temp > 35 else "Moderate temperature levels" if temp > 30 else "Cooler conditions preserving moisture"}
                </div>
            </div>

            <div class="insight-box">
                <div class="insight-label">Crop Water Demand</div>
                <div class="insight-value">
                    {crop} is a {"high" if crop_water_need[crop] == 3 else "moderate" if crop_water_need[crop] == 2 else "low"} water-demand crop
                </div>
            </div>

            <div class="insight-box">
                <div class="insight-label">Soil Condition</div>
                <div class="insight-value">
                    {"Dry soil expected" if rain < 30 else "Balanced soil moisture" if rain < 70 else "Well-moistened soil conditions"}
                </div>
            </div>
        </div>
    </div>
    """

    st.markdown(
        "<div class='decision-heading'>Final Insight</div>",
        unsafe_allow_html=True
    )

    components.html(final_insight_html, height=430)