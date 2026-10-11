import streamlit as st
import pandas as pd
import joblib



st.set_page_config(
    page_title="CouponAI | Prediction System",
    page_icon="🎟️",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0f172a;
    }

    /* Main content */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Header */
    .hero {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #1e293b,
            #111827
        );
        border: 1px solid #334155;
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 17px;
    }

    /* Cards */
    .card {
        background-color: #1e293b;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #334155;
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* Result */
    .prediction-card {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        background: linear-gradient(
            135deg,
            #172554,
            #1e3a8a
        );
        border: 1px solid #3b82f6;
        margin-top: 25px;
    }

    .prediction-title {
        font-size: 20px;
        color: #bfdbfe;
    }

    .prediction-result {
        font-size: 48px;
        font-weight: 900;
        margin: 10px 0;
    }

    .prediction-probability {
        font-size: 24px;
        color: #bfdbfe;
    }

    /* Section headers */
    .section-title {
        font-size: 24px;
        font-weight: 750;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 50px;
        padding: 20px;
    }

</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():

    preprocessor = joblib.load(
        "models/preprocessor.pkl"
    )

    model = joblib.load(
        "models/random_forest_coupon_model.pkl"
    )

    return preprocessor, model


preprocessor, model = load_model()



with st.sidebar:

    st.markdown("## 🎟️ CouponAI")

    st.markdown("---")

    st.markdown("### 🤖 Model")

    st.success("Random Forest")

    st.markdown("### 📊 Performance")

    st.metric(
        "Accuracy",
        "75.72%"
    )

    st.metric(
        "ROC-AUC",
        "81.57%"
    )

    st.markdown("---")

    st.info(
        "This application predicts whether "
        "a customer is likely to accept a coupon "
        "based on customer and travel information."
    )



st.markdown("""
<div class="hero">

<div class="hero-title">
🎟️ Coupon Acceptance Predictor
</div>

<div class="hero-subtitle">
AI-powered customer coupon acceptance prediction system
</div>

</div>
""", unsafe_allow_html=True)



col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "🤖 Model",
        "Random Forest"
    )

with col2:

    st.metric(
        "🎯 Accuracy",
        "75.72%"
    )

with col3:

    st.metric(
        "📈 ROC-AUC",
        "81.57%"
    )

with col4:

    st.metric(
        "🔢 Features",
        "23"
    )




st.markdown(
    '<div class="section-title">👤 Customer Profile</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    destination = st.selectbox(
        "📍 Destination",
        [
            "No Urgent Place",
            "Home",
            "Work"
        ]
    )

    passenger = st.selectbox(
        "👥 Passenger",
        [
            "Alone",
            "Friend(s)",
            "Kid(s)",
            "Partner"
        ]
    )

    gender = st.selectbox(
        "⚧ Gender",
        [
            "Male",
            "Female"
        ]
    )


with col2:

    age = st.selectbox(
        "🎂 Age",
        [
            "21",
            "26",
            "31",
            "36",
            "41",
            "46",
            "50plus"
        ]
    )

    marital_status = st.selectbox(
        "💍 Marital Status",
        [
            "Single",
            "Married partner",
            "Unmarried partner",
            "Divorced",
            "Widowed"
        ]
    )

    children = st.selectbox(
        "👶 Has Children?",
        [0, 1]
    )


with col3:

    education = st.selectbox(
        "🎓 Education",
        [
            "Some college - no degree",
            "Bachelors degree",
            "Graduate degree (Masters or Doctorate)",
            "High School Graduate",
            "Some High School",
            "Associates degree"
        ]
    )

    occupation = st.text_input(
        "💼 Occupation",
        "Student"
    )

    income = st.selectbox(
        "💰 Income",
        [
            "$25000 - $37499",
            "$12500 - $24999",
            "$37500 - $49999",
            "$50000 - $62499",
            "$62500 - $74999",
            "$75000 - $87499",
            "$87500 - $99999",
            "$100000 or More",
            "Less than $12500"
        ]
    )



st.markdown(
    '<div class="section-title">🎟️ Coupon Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    coupon = st.selectbox(
        "Coupon Type",
        [
            "Coffee House",
            "Restaurant(<20)",
            "Carry out & Take away",
            "Bar",
            "Restaurant(20-50)",
            "2for1 Restaurant"
        ]
    )


with col2:

    weather = st.selectbox(
        "🌤️ Weather",
        [
            "Sunny",
            "Rainy",
            "Snowy"
        ]
    )


with col3:

    expiration = st.selectbox(
        "⏱️ Expiration",
        [
            "2h",
            "1d"
        ]
    )


temperature = st.slider(
    "🌡️ Temperature",
    min_value=30,
    max_value=100,
    value=80
)




st.markdown(
    '<div class="section-title">☕ Customer Habits</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

habit_options = [
    "never",
    "less1",
    "1~3",
    "4~8",
    "gt8"
]


with col1:

    bar = st.selectbox(
        "Bar",
        habit_options
    )


with col2:

    coffee_house = st.selectbox(
        "Coffee House",
        habit_options
    )


with col3:

    carry_away = st.selectbox(
        "Carry Away",
        habit_options
    )


with col4:

    restaurant_less20 = st.selectbox(
        "Restaurant <20",
        habit_options
    )


with col5:

    restaurant_20_50 = st.selectbox(
        "Restaurant 20-50",
        habit_options
    )




st.markdown(
    '<div class="section-title">🚗 Travel Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    to_coupon_5min = st.selectbox(
        "Within 5 min",
        [0, 1]
    )


with col2:

    to_coupon_15min = st.selectbox(
        "Within 15 min",
        [0, 1]
    )


with col3:

    to_coupon_25min = st.selectbox(
        "Within 25 min",
        [0, 1]
    )


with col4:

    direction_same = st.selectbox(
        "Same Direction",
        [0, 1]
    )


with col5:

    direction_opp = st.selectbox(
        "Opposite Direction",
        [0, 1]
    )




st.markdown("---")

predict_button = st.button(
    "🔮 PREDICT COUPON ACCEPTANCE",
    use_container_width=True
)



if predict_button:

    customer = pd.DataFrame([{

        "destination": destination,
        "passanger": passenger,
        "weather": weather,
        "temperature": temperature,
        "coupon": coupon,
        "expiration": expiration,
        "gender": gender,
        "age": age,
        "maritalStatus": marital_status,
        "has_children": children,
        "education": education,
        "occupation": occupation,
        "income": income,
        "Bar": bar,
        "CoffeeHouse": coffee_house,
        "CarryAway": carry_away,
        "RestaurantLessThan20": restaurant_less20,
        "Restaurant20To50": restaurant_20_50,
        "toCoupon_GEQ5min": to_coupon_5min,
        "toCoupon_GEQ15min": to_coupon_15min,
        "toCoupon_GEQ25min": to_coupon_25min,
        "direction_same": direction_same,
        "direction_opp": direction_opp
    }])



    customer_encoded = preprocessor.transform(
        customer
    )



    prediction = model.predict(
        customer_encoded
    )[0]



    probability = model.predict_proba(
        customer_encoded
    )[0][1]


    result = (
        "ACCEPT"
        if prediction == 1
        else "REJECT"
    )


    if result == "ACCEPT":

        st.markdown(
            f"""
            <div class="prediction-card">

            <div class="prediction-title">
            🎉 PREDICTION RESULT
            </div>

            <div class="prediction-result">
            ✅ ACCEPT
            </div>

            <div class="prediction-probability">
            Acceptance Probability:
            <b>{probability * 100:.2f}%</b>
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="prediction-card">

            <div class="prediction-title">
            🎯 PREDICTION RESULT
            </div>

            <div class="prediction-result">
            ❌ REJECT
            </div>

            <div class="prediction-probability">
            Acceptance Probability:
            <b>{probability * 100:.2f}%</b>
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )




    st.markdown("### 📊 Acceptance Probability")

    st.progress(
        float(probability)
    )




st.markdown("""
<div class="footer">

🎟️ Coupon Acceptance Prediction System

<br>

Built with Python • Scikit-learn • Random Forest • Streamlit

</div>
""", unsafe_allow_html=True)