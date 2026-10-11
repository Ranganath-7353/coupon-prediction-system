import pandas as pd
import joblib


preprocessor = joblib.load(
    "models/preprocessor.pkl"
)

model = joblib.load(
    "models/random_forest_coupon_model.pkl"
)


def predict_coupon(customer_data):

    customer_df = pd.DataFrame([customer_data])

    customer_encoded = preprocessor.transform(customer_df)

    
    prediction = model.predict(customer_encoded)[0]

    probability = model.predict_proba(customer_encoded)[0][1]

    result = "ACCEPT" if prediction == 1 else "REJECT"

    return result, probability


customer = {

    "destination": "No Urgent Place",
    "passanger": "Friend(s)",
    "weather": "Sunny",
    "temperature": 80,
    "coupon": "Coffee House",
    "expiration": "1d",

    "gender": "Male",
    "age": "21",
    "maritalStatus": "Single",
    "has_children": 0,

    "education": "Bachelors degree",
    "occupation": "Student",
    "income": "$25000 - $37499",

    "Bar": "never",
    "CoffeeHouse": "1~3",
    "CarryAway": "1~3",
    "RestaurantLessThan20": "1~3",
    "Restaurant20To50": "never",

    "toCoupon_GEQ5min": 1,
    "toCoupon_GEQ15min": 0,
    "toCoupon_GEQ25min": 0,

    "direction_same": 0,
    "direction_opp": 1
}


result, probability = predict_coupon(customer)


print("      COUPON ACCEPTANCE")

print("Prediction:", result)

print(
    "Acceptance Probability:",
    round(probability * 100, 2),
    "%"
)