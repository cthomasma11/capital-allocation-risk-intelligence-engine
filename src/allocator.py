import numpy as np
from src.risk_metrics import calculate_var, calculate_cvar, calculate_drawdown

def compare_allocations(simulations_dict):
    """
    Compare multiple portfolio allocations based on risk-adjusted metrics.
    :param simulations_dict: Dictionary of portfolio simulations (key: allocation name, value: simulated results).
    :return: Sorted list of allocations based on risk-adjusted metrics (CVaR).
    """
    results = []
    for name, sims in simulations_dict.items():
        results.append({
            'allocation': name,
            'mean': np.mean(sims),  # Mean portfolio value
            'var': calculate_var(sims),  # Value at Risk (VaR)
            'cvar': calculate_cvar(sims),  # Conditional Value at Risk (CVaR)
            'drawdown': calculate_drawdown(sims)  # Maximum Drawdown
        })
    # Sort by CVaR (lower CVaR is better)
    return sorted(results, key=lambda x: x['cvar'], reverse=False)