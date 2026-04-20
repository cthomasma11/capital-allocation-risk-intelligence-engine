import pytest
from src.simulator import MonteCarloSimulator
import pandas as pd
import numpy as np

def test_simulator():
    assets = ['Asset_A', 'Asset_B', 'Asset_C']
    returns = pd.DataFrame({
        'Asset_A': np.random.normal(0.0005, 0.01, 252),
        'Asset_B': np.random.normal(0.0007, 0.015, 252),
        'Asset_C': np.random.normal(0.0003, 0.008, 252)
    })
    simulator = MonteCarloSimulator(assets, returns, num_simulations=500)
    weights = [0.4, 0.4, 0.2]
    simulations = simulator.simulate_portfolio(weights)
    assert len(simulations) == 500
    assert isinstance(simulations, np.ndarray)