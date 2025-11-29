import streamlit as st
import pandas as pd
import pickle

# Set page config
st.set_page_config(page_title="Price Prediction", layout="wide")


# Load the pre-trained model and any necessary preprocessing objects
final_model = pickle.load(open("xgboost_model.pkl", "rb"))
cars_model_te = pickle.load(open("model_te.pkl","rb"))
rto_state_te = pickle.load(open("rto_te.pkl","rb"))
global_mean = pickle.load(open('global_mean.pkl',"rb")) # Used to handle unknown categories in model

# Load the dataset for reference
df = pd.read_csv("cars_updated.csv")

# --- Page Title ---
st.markdown("""
    <h1 style='text-align: center; font-size: 45px; font-weight: 800; letter-spacing: 1px;'>
        🚗 Used Car Resale Value Range Estimator
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:18px;color:grey;'>
Provide your vehicle details to receive an accurate, data-driven resale price range.
</p>
""", unsafe_allow_html=True)



#space
st.markdown("")

# --- Input Form ---
brand = st.selectbox("Car Brand", options=sorted(df['brand'].unique().tolist()) + ['Other (Not Listed)'],
                      help="If your vehicle brand is not listed, select ‘Other (Not Listed)’ and enter it manually below.")
if brand == 'Other (Not Listed)':
    brand = st.text_input("Please specify the Car Brand")

model = st.selectbox("Car Model", options=sorted(df['model'].unique().tolist()) + ['Other (Not Listed)'],
                      help="If your vehicle model is not listed, select ‘Other (Not Listed)’ and enter it manually below.")
if model == 'Other (Not Listed)':
    model = st.text_input("Please specify the Car Model")

registration_year = st.slider("Registration Year", min_value=int(df['registration_year'].min()), max_value=int(df['registration_year'].max()), value=2015)
fuel_type = st.selectbox("Fuel Type", options=sorted(df['fuel_type'].unique()))
transmission_type = st.selectbox("Transmission Type", options=sorted(df['transmission_type'].unique()))
seats = st.number_input("Seating Capacity",min_value=2, max_value=10, step=1)
ownership = st.selectbox("Ownership (including you)",options=sorted(df['ownership'].unique()))
rto_state = st.selectbox("Registration State (RTO)", options=sorted(df['rto_state'].unique()),
             help="If your RTO state is not in the list or you're unsure, select 'Unknown'.")
engine_cc = st.number_input("Engine Capacity (CC)", min_value=0, max_value=12000, value=1500, step=50,
                            help="⚠ Enter only real engine CC values (Ex: 800–2500cc for common cars). Incorrect input will affect price accuracy."
)
mileage = st.number_input("Mileage (kmpl)", min_value=0.0, max_value=90.0, value=15.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=2500000, value=50000, step=1000)
engine_power = st.number_input("Max Engine Power (in BHP)", min_value=0.0, max_value=1300.0, step=1.0,
    help="Enter engine power in Brake Horsepower (e.g., 75, 90, 115, 150)"
)
new_vehicle_price = st.number_input("New Vehicle Price (₹ Lakhs)",min_value=0.5, max_value=1500.0, value=5.0, step=0.1,
                help="Enter the present market value/price of your current vehicle.")
has_parking_sensors = st.selectbox("Parking Sensor", ["No", "Yes"],
                                   help="If your vehicle has this feature, select Yes; otherwise select No.")
has_automatic_climate_control = st.selectbox("Automatic Climate Control", ["No", "Yes"],
                                   help="If your vehicle has this feature, select Yes; otherwise select No.")
has_rear_ac_vents = st.selectbox("Rear AC Vents", ["No", "Yes"],
                                   help="If your vehicle has this feature, select Yes; otherwise select No.")
has_central_locking = st.selectbox("Central Locking", ["No", "Yes"],
                                   help="If your vehicle has this feature, select Yes; otherwise select No.")
has_air_purifier = st.selectbox("Air Purifier", ["No", "Yes"],
                                   help="If your vehicle has this feature, select Yes; otherwise select No.")


# --- mapping the model and rto_state with Target encoded values (dict) ---

def get_te_value(value, te_dict, global_mean):
    try:
        return te_dict[value]
    except KeyError:
        return global_mean
    
model_te_value = get_te_value(model, cars_model_te, global_mean)
rto_state_te_value = get_te_value(rto_state, rto_state_te, global_mean)

# Feature Dictionary for Prediction
input_data = {
    "brand": brand,
    "registration_year": registration_year,
    "fuel_type": fuel_type,
    "seats": seats,
    "transmission_type": transmission_type,
    "ownership": ownership,
    "engine(cc)": engine_cc,
    "kms_driven": kms_driven,
    "engine_power(bhp)": engine_power,
    "mileage(kmpl)": mileage,
    "has_parking_sensors": 1 if has_parking_sensors=="Yes" else 0,
    "has_automatic_climate_control": 1 if has_automatic_climate_control=="Yes" else 0,
    "has_rear_ac_vents": 1 if has_rear_ac_vents=="Yes" else 0,
    "has_central_locking": 1 if has_central_locking=="Yes" else 0,
    "has_air_purifier": 1 if has_air_purifier=="Yes" else 0,
    "new_vehicle_price(lakhs)": new_vehicle_price,
    "model_te": model_te_value,
    "rto_te": rto_state_te_value,
}

# --- convert to DataFrame ---
input_df = pd.DataFrame([input_data])

# Centered Predict Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_btn = st.button("🚀 Predict Price", use_container_width=True)


# Prediction Output
if predict_btn:
    prediction = final_model.predict(input_df)[0]

    # Create ±2% realistic price range (your choice)
    low = prediction * 0.99
    high = prediction * 1.01

    # --- BEAUTIFUL RANGE CARD (ONLY RANGE, NO SINGLE VALUE) ---
    st.markdown("""
        <style>
        .result-card {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            padding: 26px;
            border-radius: 14px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 30px rgba(0,0,0,0.35);
            margin-top: 18px;
        }
        .range-text-main {
            font-size: 40px;
            font-weight: 900;
            color: #00e676;
        }
        .range-sub {
            font-size: 20px;
            font-weight: 600;
            margin-top: 10px;
            color: #d0f0d6;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-card">
            <div class="range-sub">Estimated Resale Value Range</div>
            <div class="range-text-main">₹ {low:.2f} - ₹ {high:.2f} Lakhs</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Rounding the prediction to 2 decimal places for database storage
    prediction = round(prediction, 2)

    # -------------------------
    # INSERT INTO POSTGRES HERE
    # -------------------------

    import psycopg2
    
    # --- Database Connection to append the predicted data to existing Postgres DB ---   

    def get_connection():
        return psycopg2.connect(
            host="localhost",
            port=5432,
            database="Cars",
            user="postgres",
            password="4568"
    )

    try:
        conn = get_connection()
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO cars_resale(
            brand, model, registration_year, fuel_type, seats, rto_state, transmission_type,
            ownership, engine_cc, kms_driven, engine_power_bhp, mileage_kmpl,
            has_parking_sensors, has_automatic_climate_control, has_rear_ac_vents,
            has_central_locking, has_air_purifier, vehicle_price_lakhs, new_vehicle_price_lakhs
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        values = (
            brand,
            model,
            registration_year,
            fuel_type,
            str(seats) +' '+ 'Seats',
            rto_state,
            transmission_type,
            ownership,
            int(engine_cc),
            int(kms_driven),
            float(engine_power),
            float(mileage),
            int(1 if has_parking_sensors=="Yes" else 0),
            int(1 if has_automatic_climate_control=="Yes" else 0),
            int(1 if has_rear_ac_vents=="Yes" else 0),
            int(1 if has_central_locking=="Yes" else 0),
            int(1 if has_air_purifier=="Yes" else 0),
            float(prediction),
            float(new_vehicle_price)
        )

        cursor.execute(insert_query, values)
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        st.error(f"Database Error: {e}")
