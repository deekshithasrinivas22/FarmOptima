import streamlit as st
import pandas as pd
import os
import numpy as np
from nav import display_navbar
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from nav import display_navbar

st.set_page_config(
    page_title="FarmOptima - Smart Crop Recommendation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

display_navbar()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Lora:wght@400;600&family=Nunito:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
    background-color: #eef4ee;
    color: #2f3a2f;
}

.main {
    background-color: #eef4ee;
}

.block-container {
    max-width: 80% !important;
    padding-top: 1rem;
    padding-bottom: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
}


h1, h2, h3 {
    font-family: 'Lora', serif;
    color: #2f3a2f;
}

[data-testid="stSidebarNav"] {
    display: none;
}

.stSelectbox label,
.stSlider label,
.stRadio label,
.stTextInput label {
    color: #9c8f7b !important;
    font-size: 11px !important;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600 !important;
}

.stSelectbox > div > div,
.stTextInput > div > div > input {
    background: #f7f3ec !important;
    border: 1px solid #ddd2c4 !important;
    border-radius: 12px !important;
    color: #2f3a2f !important;
}



# REPLACE YOUR CURRENT BUTTON CSS WITH THIS
div.stButton > button {
    background: transparent !important;
    border: none !important;
    color: #6f6658 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    margin-left: 0px !important;
    margin-top: 5px !important;
    padding: 0px !important;
    transition: 0.2s ease !important;
    box-shadow: none !important;
    white-space: nowrap !important;
    min-width: max-content !important;
}

div.stButton > button:hover {
    background: transparent !important;
    color: #3a5c38 !important;
}

div.stButton > button[kind="primary"] {
    background: #2d4c2d !important;
    color: white !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 0.9rem 2rem !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    width: 260px !important;
}

div.stButton > button[kind="primary"]:hover {
    background: #1f381f !important;
    color: white !important;
}

.section-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: #a89b89;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid #d9d2c6;
}

.metric-card {
    background: #f7f3ec;
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 1rem;
}

.metric-label {
    font-size: 12px;
    color: #8b7d69;
    margin-bottom: 0.4rem;
}

.metric-value {
    font-size: 30px;
    font-family: 'Lora', serif;
    color: #2f3a2f;
}

.soil-card {
    background: #f7f3ec;
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.2rem;
    text-align: center;
    margin-top: 0.5rem;
}

.soil-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #9c8f7b;
}

.soil-value {
    font-size: 32px;
    font-family: 'Lora', serif;
    color: #2f3a2f;
    margin-top: 0.4rem;
}

.crop-card {
    background: #f7f3ec;
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 1rem;
}

.crop-rank {
    font-size: 11px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #a89b89;
}

.crop-title {
    font-size: 28px;
    font-family: 'Lora', serif;
    color: #2f3a2f;
    margin-top: 0.4rem;
}

.crop-sub {
    color: #8b7d69;
    font-size: 13px;
    margin-top: 0.4rem;
}

.status-card {
    border-radius: 18px;
    padding: 1.3rem;
    margin-bottom: 1rem;
    border-left: 5px solid;
}

.status-card.green {
    background: #e5efe3;
    border-color: #4a7c42;
}

.status-card.yellow {
    background: #f8efdf;
    border-color: #ba7517;
}

.status-card.red {
    background: #f8e3e0;
    border-color: #c84d3a;
}

.status-title {
    font-size: 20px;
    font-family: 'Lora', serif;
    color: #2f3a2f;
    margin-bottom: 0.5rem;
}

.status-subtitle {
    font-size: 14px;
    color: #5d564d;
    line-height: 1.7;
}

.why-card {
    background: #f7f3ec;
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.2rem 1.5rem;
}

.why-row {
    display: flex;
    justify-content: space-between;
    padding: 0.9rem 0;
    border-bottom: 1px solid #ddd2c4;
}

.why-row:last-child {
    border-bottom: none;
}

.why-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #9c8f7b;
    font-weight: 700;
}

.why-value {
    font-size: 18px;
    color: #2f3a2f;
    font-family: 'Lora', serif;
}

.footer-box {
    background: #f7f3ec;
    border: 1px solid #ddd2c4;
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    margin-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer-text {
    color: #8b7d69;
    font-size: 13px;
}

.footer-badge {
    background: #e5efe3;
    color: #3a5c38;
    padding: 8px 16px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# header
st.markdown("""
<div style='margin-bottom:2rem;'>
    <div style='font-size:11px; letter-spacing:0.22em; text-transform:uppercase; color:#a89b89; font-weight:600;'>
        Crop Recommendation
    </div>
    <h1 style='font-size:48px; margin-bottom:0.4rem;'>
        Find the right crop for your land
    </h1>
    <p style='color:#8b7d69; font-size:15px; max-width:700px;'>
        Enter your farm details and get crop recommendations based on weather, season, soil nutrients and farm size.
    </p>
</div>
""", unsafe_allow_html=True)

#weather
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

    return temp, max(rain, 0)

# data
@st.cache_resource
def load_data():
    crop = pd.read_csv("dataset/crop.csv").dropna()

    le_state = LabelEncoder()
    le_season = LabelEncoder()
    le_crop = LabelEncoder()

    crop["State_Name"] = le_state.fit_transform(crop["State_Name"])
    crop["Season"] = le_season.fit_transform(crop["Season"])
    crop["Crop"] = le_crop.fit_transform(crop["Crop"])

    X = crop[["State_Name", "Season", "Crop_Year", "Area"]]
    y = crop["Crop"]

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)

    return model, le_state, le_season, le_crop

model, le_state, le_season, le_crop = load_data()

#farm
st.markdown("<div class='section-title'>Farm Details</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    state = st.selectbox("State", le_state.classes_)

with col2:
    season = st.selectbox("Season", le_season.classes_)

with col3:
    year = st.selectbox("Year", list(range(2000, 2031)))

with col4:
    area = st.slider("Area (acres)", 1, 100, 10)

# weather display
temp, rain = weather(state, season)

w1, w2 = st.columns(2)

with w1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-label'>Temperature</div>
        <div class='metric-value'>{temp}°C</div>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-label'>Rainfall</div>
        <div class='metric-value'>{rain} mm</div>
    </div>
    """, unsafe_allow_html=True)

# soil
st.markdown("<div class='section-title'>Soil Data</div>", unsafe_allow_html=True)

soil_mode = st.radio(
    "Soil Data Source",
    ["Use Default Soil Data", "Enter Custom Soil Data"]
)

if soil_mode == "Enter Custom Soil Data":

    s1, s2, s3 = st.columns(3)

    with s1:
        n_input = st.text_input("Nitrogen (%)", placeholder="50")

    with s2:
        p_input = st.text_input("Phosphorus (%)", placeholder="40")

    with s3:
        k_input = st.text_input("Potassium (%)", placeholder="45")

    try:
        n_percent = float(n_input) if n_input else 50
        p_percent = float(p_input) if p_input else 50
        k_percent = float(k_input) if k_input else 50
    except:
        st.error("Please enter valid nutrient values")
        st.stop()

else:
    n_percent = 60
    p_percent = 60
    k_percent = 60

soil1, soil2, soil3 = st.columns(3)

with soil1:
    st.markdown(f"""
    <div class='soil-card'>
        <div class='soil-label'>Nitrogen</div>
        <div class='soil-value'>{int(n_percent)}%</div>
    </div>
    """, unsafe_allow_html=True)

with soil2:
    st.markdown(f"""
    <div class='soil-card'>
        <div class='soil-label'>Phosphorus</div>
        <div class='soil-value'>{int(p_percent)}%</div>
    </div>
    """, unsafe_allow_html=True)

with soil3:
    st.markdown(f"""
    <div class='soil-card'>
        <div class='soil-label'>Potassium</div>
        <div class='soil-value'>{int(k_percent)}%</div>
    </div>
    """, unsafe_allow_html=True)

#button
st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

if st.button("Get Recommendation", type="primary"):
    state_enc = le_state.transform([state])[0]
    season_enc = le_season.transform([season])[0]

    probs = model.predict_proba([[state_enc, season_enc, year, area]])[0]

    soil_score = (n_percent + p_percent + k_percent) / 3

    adjusted_probs = []

    for prob in probs:
        score = prob

        if soil_score > 70:
            score += 0.05
        elif soil_score < 30:
            score -= 0.05

        if temp > 35:
            score -= 0.03

        if rain < 30:
            score -= 0.04

        adjusted_probs.append(score)

    adjusted_probs = np.array(adjusted_probs)

    top3_idx = adjusted_probs.argsort()[-3:][::-1]
    top_crops = le_crop.inverse_transform(top3_idx)
    confidence = adjusted_probs[top3_idx[0]] * 100

    st.markdown("<div class='section-title'>Top Crop Recommendations</div>", unsafe_allow_html=True)

    descriptions = [
        "Strongest match for your inputs",
        "Good fit with slightly lower confidence",
        "Consider if conditions improve"
    ]

    crop_cols = st.columns(3)

    for i, crop_name in enumerate(top_crops):
        with crop_cols[i]:
            st.markdown(f"""
            <div class='crop-card'>
                <div class='crop-rank'>Pick {i+1}</div>
                <div class='crop-title'>{crop_name}</div>
                <div class='crop-sub'>{descriptions[i]}</div>
            </div>
            """, unsafe_allow_html=True)

            img_path = f"images/{crop_name.lower().split()[0]}.jpg"

            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.image("images/default.jpg", use_container_width=True)

    st.markdown("<div class='section-title'>Model Confidence</div>", unsafe_allow_html=True)
    st.progress(min(int(confidence), 100))
    st.markdown(f"<h2 style='margin-top:0.5rem;'>{confidence:.1f}% confidence score</h2>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Soil Analysis</div>", unsafe_allow_html=True)

    if soil_score < 30:
        st.markdown("""
        <div class='status-card red'>
            <div class='status-title'>Low Soil Fertility</div>
            <div class='status-subtitle'>
                Nutrient availability is poor. Add compost or fertiliser before sowing.
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif soil_score < 70:
        st.markdown("""
        <div class='status-card yellow'>
            <div class='status-title'>Moderate Soil Fertility</div>
            <div class='status-subtitle'>
                Soil nutrients are moderate. Use fertiliser for better crop yield.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class='status-card green'>
            <div class='status-title'>High Soil Fertility</div>
            <div class='status-subtitle'>
                Soil nutrients are strong and suitable for healthy crop growth.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Risk & Conditions</div>", unsafe_allow_html=True)

    if rain < 30:
        st.markdown(f"""
        <div class='status-card red'>
            <div class='status-title'>Drought Risk</div>
            <div class='status-subtitle'>
                Rainfall is very low at {rain} mm.<br><br>
                Increase irrigation and avoid water-intensive crops.
            </div>
        </div>
        """, unsafe_allow_html=True)
    elif rain > 150:
        st.markdown(f"""
        <div class='status-card yellow'>
            <div class='status-title'>Flood Risk</div>
            <div class='status-subtitle'>
                Rainfall is very high at {rain} mm.<br><br>
                Improve drainage and avoid waterlogging.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='status-card green'>
            <div class='status-title'>Stable Rainfall</div>
            <div class='status-subtitle'>
                Rainfall is currently balanced at {rain} mm.<br><br>
                Conditions are suitable for healthy crop growth.
            </div>
        </div>
        """, unsafe_allow_html=True)

    if temp > 35:
        st.markdown(f"""
        <div class='status-card yellow'>
            <div class='status-title'>High Temperature</div>
            <div class='status-subtitle'>
                Temperature is {temp}°C.<br><br>
                Crops may experience heat stress and need additional watering.
            </div>
        </div>
        """, unsafe_allow_html=True)
    elif temp < 20:
        st.markdown(f"""
        <div class='status-card yellow'>
            <div class='status-title'>Low Temperature</div>
            <div class='status-subtitle'>
                Temperature is {temp}°C.<br><br>
                Cold-sensitive crops may require protection.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='status-card green'>
            <div class='status-title'>Optimal Temperature</div>
            <div class='status-subtitle'>
                Temperature is ideal for crop development at {temp}°C.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Why These Crops?</div>", unsafe_allow_html=True)

    why1, why2 = st.columns(2)

    with why1:
        st.markdown(f"""
        <div class='why-card'>
            <div class='why-row'>
                <div class='why-label'>Location</div>
                <div class='why-value'>{state}</div>
            </div>
            <div class='why-row'>
                <div class='why-label'>Season</div>
                <div class='why-value'>{season}</div>
            </div>
            <div class='why-row'>
                <div class='why-label'>Farm Size</div>
                <div class='why-value'>{area} acres</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with why2:
        st.markdown(f"""
        <div class='why-card'>
            <div class='why-row'>
                <div class='why-label'>Temperature</div>
                <div class='why-value'>{temp}°C</div>
            </div>
            <div class='why-row'>
                <div class='why-label'>Rainfall</div>
                <div class='why-value'>{rain} mm</div>
            </div>
            <div class='why-row'>
                <div class='why-label'>Soil NPK</div>
                <div class='why-value'>{int(n_percent)} / {int(p_percent)} / {int(k_percent)}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class='footer-box'>
    <div class='footer-text'>
        Helping farmers make smarter decisions — one data point at a time.
    </div>
    <div class='footer-badge'>
        AI-powered
    </div>
</div>
""", unsafe_allow_html=True)

