import streamlit as st
import numpy as np
from heatmap_plot import generate_option_prices, plot_heatmap

# App Title
st.set_page_config(page_title="OptiPricer - Option Pricing Heatmap", layout="wide")
st.title("📈 Black-Scholes Option Pricing - Call & Put Heatmaps")

# Sidebar Inputs
st.sidebar.header("Option Parameters")
K = st.sidebar.number_input("Strike Price (K)", value=100.0)
T = st.sidebar.number_input("Time to Maturity (T in years)", value=1.0, format="%.2f")
r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05, format="%.2f")

spot_prices = np.linspace(80, 120, 10)
volatilities = np.linspace(0.1, 0.8, 10)

# Generate Prices
call_prices, put_prices = generate_option_prices(spot_prices, volatilities, K, T, r)

# Plot Heatmaps
st.subheader("Call Price Heatmap")
fig1 = plot_heatmap(call_prices, spot_prices, volatilities, "Call Option Price Heatmap", "viridis", "Call Price")
st.pyplot(fig1)

st.subheader("Put Price Heatmap")
fig2 = plot_heatmap(put_prices, spot_prices, volatilities, "Put Option Price Heatmap", "viridis", "Put Price")
st.pyplot(fig2)

st.success("✅ Interactive Heatmaps Generated Successfully!")
