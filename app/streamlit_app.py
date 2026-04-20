import streamlit as st
import numpy as np
import pandas as pd
from src.simulator import MonteCarloSimulator

# Set up the Streamlit app
st.title("Portfolio Risk Simulation")

# Inputs for portfolio weights
allocation_A = st.slider("Allocation in Asset A", 0.0, 1.0, 0.4)
allocation_B = st.slider("Allocation in Asset B", 0.0, 1.0, 0.4)
weights = [allocation_A, allocation_B]

# Example data for assets
returns = pd.DataFrame({
    'Asset_A': np.random.normal(0.0005, 0.01, 252),
    'Asset_B': np.random.normal(0.0007, 0.015, 252)
})

# Simulate portfolio returns using the Monte Carlo simulation
simulator = MonteCarloSimulator(assets=['Asset_A', 'Asset_B'], returns_df=returns[['Asset_A', 'Asset_B']], num_simulations=1000, horizon=252)
simulations = simulator.simulate_portfolio(weights)

# Display the results in Streamlit
st.write("Simulated Portfolio Final Value Distribution")
st.histogram(simulations)  # Displaying histogram of simulated portfolio values