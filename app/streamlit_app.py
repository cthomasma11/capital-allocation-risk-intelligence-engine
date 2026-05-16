import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from src.simulator import MonteCarloSimulator
from src.risk_metrics import calculate_var, calculate_cvar, calculate_drawdown

st.title("Capital Allocation & Risk Intelligence Engine")

st.write(
    "Monte Carlo simulation dashboard for evaluating portfolio risk, downside exposure, "
    "and capital allocation outcomes."
)

# Example simulation data
np.random.seed(42)
simulations = np.random.normal(loc=1.10, scale=0.15, size=1000)

# Risk metrics
var_95 = calculate_var(simulations, alpha=0.05)
cvar_95 = calculate_cvar(simulations, alpha=0.05)
max_drawdown = calculate_drawdown(simulations)

st.subheader("Risk Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("VaR 95%", f"{var_95:.4f}")
col2.metric("CVaR 95%", f"{cvar_95:.4f}")
col3.metric("Max Drawdown", f"{max_drawdown:.4f}")

st.subheader("Distribution of Final Portfolio Values")

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(simulations, bins=30, alpha=0.7)
ax.axvline(var_95, linestyle="--", label="VaR 95%")
ax.axvline(cvar_95, linestyle="--", label="CVaR 95%")
ax.set_title("Distribution of Final Portfolio Values")
ax.set_xlabel("Final Portfolio Value")
ax.set_ylabel("Frequency")
ax.legend()
ax.grid(True)

st.pyplot(fig)