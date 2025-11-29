import streamlit as st

st.set_page_config(page_title="Used Car Valuation Portal", layout="wide")

# =========================================================
# MAIN TITLE
# =========================================================
st.markdown("""
<h1 style="text-align:center;font-size:48px;color:#0B4F6C;font-weight:900;">
🚗 Used Cars Market Analytics & Price Estimation System
</h1>
<p style="text-align:center;font-size:19px;color:#4A4A4A;">
A complete platform to explore used-car market insights and estimate fair resale price ranges using AI.
</p>
""", unsafe_allow_html=True)

st.write("---")

# =========================================================
# PAGE-1 : ANALYTICS DASHBOARD SUMMARY
# =========================================================
st.markdown("""
### 📊 Page 1 — Used Cars Market Analytics Dashboard
 
An interactive dashboard designed to study the used-car market visually.

#### 🔹 How each chart helps you
| Chart | What it Shows | Why it Matters |
|---|---|---|
| 💰 Price Distribution | Common selling price ranges | Helps know what pricing is normal in market |
| 🏷️ Brand-wise Avg Price | Best priced brands on average | Reveals strong resale value brands |
| 🔁 Ownership vs Price | Impact of owner count on price | Helps judge if 2nd/3rd owner is worth buying |
| 🚗 KM Driven vs Price Scatter | Running distance vs value drop | Helps know ideal price for high km cars |
| ⛽ Mileage by Brand | Fuel efficiency comparison | Buyers pick economical cars easily |
| 📅 Year vs Price Trend | Resale value over time | Shows how the resale price shifts as cars age |

<small style="color:grey;">Filter and compare brands, states, fuel types, years & other factors instantly.</small>
""", unsafe_allow_html=True)

st.write("---")

# =========================================================
# PAGE-2 : PRICE PREDICTION SUMMARY
# =========================================================
st.markdown("""
### 💵 Page 2 —  Used Car Resale Value Range Estimator

Enter vehicle details → Get a realistic **minimum–maximum expected selling price**.

#### Why price is given as a range?
Because final price varies based on:
- Condition
- Region
- Market demand
- Mileage & features

A range gives a **fair and practical estimate** instead of a fixed guess.
""")

st.write("---")

# =========================================================
# HOW USERS CAN USE THIS SYSTEM
# =========================================================
st.markdown("""
### 🧑‍💼 For Buyers
- Compare prices across brands, ownerships & years using dashboard  
- Check how KM driven, ownership & mileage affect value  
- Helps decide which region/state gives better price for same car
- Use the prediction range to verify if seller price is fair  
- Helps avoid paying extra during negotiation

#### Buyer Example  
Car listed at ₹9L → Prediction range says ₹7.8–₹8.4L  
➡ Buyer knows seller is charging higher → can negotiate confidently.

---

### 🏷️ For Sellers
- Know ideal selling range before listing online  
- Understand how mileage and other features affect price
- Helps understand how much more they can demand in their state
- Price competitively without under-selling  
- Strong mileage or condition = Price can be set at upper range

#### Seller Example  
App predicts ₹4.2–₹4.6L  
➡ Seller lists around upper range ₹4.5L confidently without loss.
""")

st.write("---")

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<p style="text-align:center;color:#6E6E6E;margin-top:30px;font-size:14px;">
Built using Machine Learning • Real Market Data • Designed for Buyers & Sellers
</p>
""", unsafe_allow_html=True)
