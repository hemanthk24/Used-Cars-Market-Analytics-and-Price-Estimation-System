
# --- USED CAR ANALYTICS DASHBOARD ----


import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics Dashboard", layout="wide")


# Load Data
df = pd.read_csv("cars_updated.csv")


# ---- CUSTOM UI STYLING -----

st.markdown("""
<style>
    .plot-card {
        background: #ffffff;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0px 3px 15px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }
    .metric-card {
        background: linear-gradient(135deg,#4e73df,#224abe);
        padding: 20px;
        color: white;
        border-radius: 14px;
        text-align:center;
        font-size:20px;
        font-weight:bold;
        margin-bottom:18px;
        box-shadow:0 4px 10px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)


# ---- SIDEBAR FILTERS ----

st.sidebar.header("🔍 Filter Data")

brand_filter = st.sidebar.multiselect("Brand", options=sorted(df['brand'].unique()), default=sorted(df['brand'].value_counts().index[:6].tolist()))
ownership_filter = st.sidebar.multiselect("Ownership", df['ownership'].unique(), default=df['ownership'].unique())
year_range = st.sidebar.slider("Registration Year", int(df.registration_year.min()), int(df.registration_year.max()), (2010,2022))
fuel_filter = st.sidebar.multiselect("Fuel Type", df['fuel_type'].unique(), default=df['fuel_type'].unique())
rto_filter = st.sidebar.multiselect("RTO State", df['rto_state'].unique(), default=sorted(df['rto_state'].value_counts().index[:1].tolist()))
trans_filter = st.sidebar.multiselect("Transmission", df['transmission_type'].unique(), default=df['transmission_type'].unique())

df_filtered = df[
    (df['brand'].isin(brand_filter)) &
    (df['ownership'].isin(ownership_filter)) &
    (df['registration_year'].between(year_range[0], year_range[1])) &
    (df['fuel_type'].isin(fuel_filter)) &
    (df['rto_state'].isin(rto_filter)) &
    (df['transmission_type'].isin(trans_filter))
]


# ----- PAGE TITLE ------

st.markdown("<h1 style='text-align:center;color:#0B4F6C;'>🏎️ Used Cars Market Analytics Dashboard</h1>", unsafe_allow_html=True)
st.write(" ")

st.markdown("<p style='text-align:center;font-size:19px;'>A modern visual overview of car resale pricing trends, brand value, market usage behavior and performance insights.</p>", unsafe_allow_html=True)
st.write("---")


# ---  KPI METRICS SECTION ---

km1, km2, km3 = st.columns(3)
km1.markdown(f"<div class='metric-card'>📌 Total Cars<br>{len(df):,}</div>", unsafe_allow_html=True)
km2.markdown(f"<div class='metric-card'>💰 Avg Price<br>{df['vehicle_price(lakhs)'].mean():.2f} Lakhs</div>", unsafe_allow_html=True)
km3.markdown(f"<div class='metric-card'>⛽ Avg Mileage<br>{df['mileage(kmpl)'].mean():.1f} kmpl</div>", unsafe_allow_html=True)

st.markdown(f"🔥 Showing <b>{len(df_filtered):,}</b> cars after filter selection", unsafe_allow_html=True)
st.write(" ")


# --- PLOTS -----

# ROW 1
c1, c2 = st.columns(2)

with c1:
    st.markdown("<h3 style='text-align:center;'>💰 Resale Price Distribution</h3>", unsafe_allow_html=True)
    fig1 = px.histogram(df_filtered,
                        x="vehicle_price(lakhs)",
                        nbins=50,marginal="box",
                        labels={"vehicle_price(lakhs)":"Resale Price (Lakhs)","count":"Cars"},
                        color_discrete_sequence=['#A4E03F'])
    st.plotly_chart(fig1,width="stretch")

with c2:
    st.markdown("<h3 style='text-align:center;'>🏷️ Average Resale Price by Brand</h3>", unsafe_allow_html=True)
    avg_brand = df_filtered.groupby("brand")["vehicle_price(lakhs)"].mean().reset_index().sort_values("vehicle_price(lakhs)",ascending=False).head(15)
    fig2 = px.bar(avg_brand,
                  x="brand",
                  y="vehicle_price(lakhs)",
                  color="vehicle_price(lakhs)",
                  labels={'vehicle_price(lakhs)': 'Avg Resale Price (lakhs)', 'brand': 'Brand'},
                  color_continuous_scale="Viridis")
    st.plotly_chart(fig2,width="stretch")

# ROW 2
c3, c4 = st.columns(2)

with c3:
    st.markdown("<h3 style='text-align:center;'>🔁 Ownership History Impact on Price</h3>", unsafe_allow_html=True)
    df_owner = df_filtered.groupby("ownership")["vehicle_price(lakhs)"].mean().reset_index()
    fig3 = px.line(df_owner,
                   x="ownership",
                   y="vehicle_price(lakhs)",
                   markers=True, 
                   labels={'vehicle_price(lakhs)': 'Avg Resale Price (lakhs)', 'ownership': 'Ownership'},)
    st.plotly_chart(fig3,width="stretch")

with c4:
    st.markdown("<h3 style='text-align:center;'>🚗 KM's Driven vs Resale Price</h3>", unsafe_allow_html=True)
    fig4 = px.scatter(df_filtered,
                      x="kms_driven",
                      y="vehicle_price(lakhs)",
                      color="vehicle_price(lakhs)",
                      labels={'vehicle_price(lakhs)': 'Vehicle Resale Price (Lakhs)', 'kms_driven': 'Kilometers Driven'},
                      color_continuous_scale="Viridis")
    st.plotly_chart(fig4,width="stretch")

# ROW 3
c5, c6 = st.columns(2)

with c5:
    st.markdown("<h3 style='text-align:center;'>⛽ Average Mileage by Brand</h3>", unsafe_allow_html=True)
    avg_mil = df_filtered.groupby("brand")["mileage(kmpl)"].mean().reset_index().sort_values("mileage(kmpl)",ascending=False)
    fig5 = px.bar(avg_mil,x="brand",
                  y="mileage(kmpl)",
                  color="mileage(kmpl)",
                  color_continuous_scale="Viridis",
                  labels={'mileage(kmpl)': 'Avg Mileage (kmpl)', 'brand': 'Brand'})
    st.plotly_chart(fig5,width="stretch")


with c6:
    st.markdown("<h3 style='text-align:center;'>📅 Price Trend Across Registration Years</h3>", unsafe_allow_html=True)
    fig6 = px.scatter(df_filtered,
                      x="registration_year",
                      y="vehicle_price(lakhs)",
                      color="vehicle_price(lakhs)",
                      color_continuous_scale="Plasma",
                      labels={'vehicle_price(lakhs)': 'Vehicle Resale Price (Lakhs)', 'registration_year': 'Registration Year'})
    st.plotly_chart(fig6,width="stretch")

# ----- FOOTER NOTE -----
st.markdown("""
<div style="
    background: #f5f7fa;
    padding: 12px 18px;
    border-left: 6px solid #0b4f6c;
    border-radius: 6px;
    font-size: 15.5px;
    margin-top: -10px;
    color:#2c3e50;
">
<b>Note:</b> The dashboard displays brand-level trends from historical data.
Actual vehicle resale price may vary based on specific model, engine power,
features, condition, maintenance history, and modifications.
</div>
""", unsafe_allow_html=True)
