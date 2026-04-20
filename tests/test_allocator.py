import pytest
import numpy as np
from src.allocator import compare_allocations

def test_compare_allocations():
    # Simulate two allocations: conservative (60% Asset_A, 30% Asset_B, 10% Asset_C)
    # and aggressive (30% Asset_A, 50% Asset_B, 20% Asset_C)
    simulations_conservative = np.random.normal(0.0005, 0.01, 1000)
    simulations_aggressive = np.random.normal(0.0007, 0.015, 1000)

    simulations_dict = {
        'Conservative': simulations_conservative,
        'Aggressive': simulations_aggressive
    }

    # Compare allocations
    results = compare_allocations(simulations_dict)

    # Check if results are sorted by CVaR (lower CVaR should be ranked higher)
    assert results[0]['allocation'] == 'Aggressive'
    assert results[1]['allocation'] == 'Conservative'

    # Ensure that the results contain key metrics (mean, VaR, CVaR, drawdown)
    assert 'mean' in results[0]
    assert 'cvar' in results[0]
    assert 'drawdown' in results[0]