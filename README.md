# Used Cars Market Analytics & Price Estimation System

A full end-to-end machine learning project that analyzes the Indian used-car market and predicts fair resale price ranges.  
The system provides an analytical dashboard for insights and a price-prediction engine powered by XGBoost.

Web app Url : https://used-car-valuation.streamlit.app/
---

## Project Overview

Used-car pricing varies widely based on multiple factors like brand, mileage, age, fuel type, RTO state, and ownership.  
This project solves the problem by:

- Analyzing **8000+ car listings**
- Extracting market patterns using EDA
- Predicting realistic price-ranges instead of a single value
- Deploying an interactive Streamlit application

---

## Features

| Component | Description |
|---|---|
| 📊 Analytics Dashboard | Explore market behavior using filters and charts |
| 🧠 Machine Learning Model | Predicts price range using XGBoost |
| 🎯 Target Encoding | Handles categorical variables effectively |
| 🏷 State & Brand Comparison | Understand pricing differences across India |
| 📈 Trend Visualizations | Year, KM, Ownership impact insights |
| 🌐 Live App UI | User-friendly Streamlit web interface |

---

##  Dashboard Insights (Page-1)

The dashboard provides deep analytical understanding of resale trends.

| Chart | What You Learn | Why It Matters |
|---|---|---|
| 💰 Price Distribution | Common selling price bands | Helps buyers & sellers benchmark |
| 🏷 Avg Price by Brand | Best resale-value brands | Identify high-value brands |
| 🔁 Ownership vs Price | Depreciation with more owners | Fair-value negotiation clarity |
| 🚗 KM Driven vs Price | Mileage impact on resale | Avoid overpriced high-km cars |
| ⛽ Mileage by Brand | Efficiency comparison | Helps budget-friendly buyers |
| 📅 Registration Year Trend | Depreciation vs age | Helps choose value-optimized cars |

**Available Filters:** Brand • Fuel-Type • RTO-State • Ownership • Transmission • Registration Year

---

##  Price Prediction (Page-2)

Users enter car features → model outputs a **realistic price-range** instead of a single fixed number.

Why range-based pricing?

- Condition varies drastically for same model
- Mileage, servicing & accidents change valuation
- Location-based demand affects resale price

**Model:** `XGBoost Regressor`

---

## Machine Learning Workflow

1. Data Cleaning & Outlier removal  
2. Feature Engineering  
3. Target Encoding for categorical features  
4. Model testing — Linear, DT, RF & XGBoost  
5. XGBoost chosen for highest accuracy  
6. Model exported as `.pkl` for deployment

---

## 🏁 Run Project Locally

```bash
git clone <repository-url>
cd Used-Car-Valuation-System

pip install -r requirements.txt
streamlit run app.py

