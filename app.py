import streamlit as st
import pandas as pd
import pickle

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# ====================================
# LOAD MODEL
# ====================================

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))
df = pd.read_csv("cardekho_dataset.csv")

# ====================================
# CUSTOM CSS
# ====================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #16213e,
        #243b55
    );
}

/* Page spacing */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

/* Hero Title */

.hero-title{
    text-align:center;
    color:white;
    font-size:72px;
    font-weight:800;
    margin-bottom:10px;
}

.hero-subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:30px;
    margin-bottom:50px;
}

/* Card */

.glass-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    padding:35px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0px 10px 30px rgba(0,0,0,0.3);
}

/* Labels */

.big-label{
    color:white;
    font-size:24px;
    font-weight:700;
    margin-bottom:10px;
    margin-top:15px;
}

/* Button */

.stButton > button{
    width:100%;
    height:70px;
    border:none;
    border-radius:18px;
    background:linear-gradient(
        90deg,
        #22c55e,
        #16a34a
    );
    color:white;
    font-size:24px;
    font-weight:700;
    font-weight:bold;
}

.stButton > button:hover{
    transform:scale(1.02);
}

/* Metrics */

.metric-card{
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
}

/* Result */

.result-card{
    background: linear-gradient(
        135deg,
        #16a34a,
        #22c55e
    );

    padding:40px;
    border-radius:25px;

    text-align:center;
    color:white;

    margin-top:25px;

    box-shadow:0px 10px 30px rgba(0,0,0,0.35);
}

.result-price{
    font-size:60px;
    font-weight:800;
}

.result-text{
    font-size:24px;
}

.footer{
    text-align:center;
    color:#cbd5e1;
    margin-top:50px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ====================================
# HERO SECTION
# ====================================

st.markdown("""
<div class="hero-title">
🚗 Used Car Price Prediction System
</div>

<div class="hero-subtitle">
Predict the Resale Value of Your Vehicle Using Machine Learning
</div>
""", unsafe_allow_html=True)

# ====================================
# STATS
# ====================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-card">
    <h2>15,244+</h2>
    Cars Analyzed
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
    <h2>283</h2>
    Features Used
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
    <h2>89%</h2>
    Model Accuracy
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ====================================
# FORM CARD
# ====================================


left, right = st.columns(2)

# ====================================
# LEFT SIDE
# ====================================

with left:

    st.markdown('<div class="big-label">🏷 Brand</div>', unsafe_allow_html=True)
    brand = st.selectbox(
        "",
        sorted(df["brand"].unique()),
        label_visibility="collapsed"
    )

    filtered_models = sorted(
        df[df["brand"] == brand]["model"].unique()
    )

    st.markdown('<div class="big-label">🚘 Model</div>', unsafe_allow_html=True)
    model_name = st.selectbox(
        "",
        filtered_models,
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">👤 Seller Type</div>', unsafe_allow_html=True)
    seller_type = st.selectbox(
        "",
        sorted(df["seller_type"].unique()),
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">⛽ Fuel Type</div>', unsafe_allow_html=True)
    fuel_type = st.selectbox(
        "",
        sorted(df["fuel_type"].unique()),
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">⚙ Transmission Type</div>', unsafe_allow_html=True)
    transmission_type = st.selectbox(
        "",
        sorted(df["transmission_type"].unique()),
        label_visibility="collapsed"
    )

# ====================================
# RIGHT SIDE
# ====================================

with right:

    st.markdown('<div class="big-label">📅 Vehicle Age (Years)</div>', unsafe_allow_html=True)
    vehicle_age = st.number_input(
        "",
        min_value=0,
        max_value=30,
        value=5,
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">🛣 KM Driven</div>', unsafe_allow_html=True)
    km_driven = st.number_input(
        "",
        min_value=0,
        value=50000,
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">⛽ Mileage (km/l)</div>', unsafe_allow_html=True)
    mileage = st.number_input(
        "",
        min_value=0.0,
        value=18.0,
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">🔧 Engine Capacity (CC)</div>', unsafe_allow_html=True)
    engine = st.number_input(
        "",
        min_value=500,
        value=1200,
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">🔥 Max Power (HP)</div>', unsafe_allow_html=True)
    max_power = st.number_input(
        "",
        min_value=20.0,
        value=80.0,
        label_visibility="collapsed"
    )

    st.markdown('<div class="big-label">💺 Number of Seats</div>', unsafe_allow_html=True)
    seats = st.number_input(
        "",
        min_value=2,
        max_value=10,
        value=5,
        label_visibility="collapsed"
    )

predict_btn = st.button("🚀 Predict Car Price")



# ====================================
# PREDICTION
# ====================================

if predict_btn:

    sample = pd.DataFrame(columns=columns)
    sample.loc[0] = 0

    sample["vehicle_age"] = vehicle_age
    sample["km_driven"] = km_driven
    sample["mileage"] = mileage
    sample["engine"] = engine
    sample["max_power"] = max_power
    sample["seats"] = seats

    brand_col = f"brand_{brand}"
    if brand_col in sample.columns:
        sample[brand_col] = 1

    model_col = f"model_{model_name}"
    if model_col in sample.columns:
        sample[model_col] = 1

    seller_col = f"seller_type_{seller_type}"
    if seller_col in sample.columns:
        sample[seller_col] = 1

    fuel_col = f"fuel_type_{fuel_type}"
    if fuel_col in sample.columns:
        sample[fuel_col] = 1

    transmission_col = f"transmission_type_{transmission_type}"
    if transmission_col in sample.columns:
        sample[transmission_col] = 1

    prediction = model.predict(sample)[0]

    st.balloons()


    st.markdown(
    f"""
    <h3 style='color:white;'>
        🚗 Estimated Market Value
    </h3>

    <h1 style='color:#22c55e;
               font-size:60px;
               font-weight:800;'>
        ₹ {prediction:,.0f}
    </h1>
    """,
    unsafe_allow_html=True
)


# ====================================
# FOOTER
# ====================================

st.markdown("""
<div class="footer">
Developed by Hetav Antani • Machine Learning Project • 2026
</div>
""", unsafe_allow_html=True)