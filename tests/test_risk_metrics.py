import pytest
import numpy as np
from src.risk_metrics import calculate_var, calculate_cvar, calculate_drawdown

def test_calculate_var():
    simulations = np.random.normal(0.0005, 0.01, 1000)  # Generate random simulated portfolio returns
    var = calculate_var(simulations, alpha=0.05)
    assert var < 0  # VaR should be a negative value
    assert isinstance(var, float)

def test_calculate_cvar():
    simulations = np.random.normal(0.0005, 0.01, 1000)
    cvar = calculate_cvar(simulations, alpha=0.05)
    assert cvar < 0  # CVaR should be a negative value
    assert isinstance(cvar, float)

def test_calculate_drawdown():
    simulations = np.random.normal(0.0005, 0.01, 1000)
    drawdown = calculate_drawdown(simulations)
    assert drawdown < 0  # Drawdown should be negative
    assert isinstance(drawdown, float)