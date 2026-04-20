import numpy as np

def calculate_var(simulations, alpha=0.05):
    """
    Calculate the Value at Risk (VaR) at a given confidence level.
    :param simulations: Simulated portfolio returns.
    :param alpha: Confidence level (default 5% for VaR).
    :return: VaR at the given confidence level.
    """
    return np.percentile(simulations, alpha * 100)

def calculate_cvar(simulations, alpha=0.05):
    """
    Calculate the Conditional Value at Risk (CVaR).
    :param simulations: Simulated portfolio returns.
    :param alpha: Confidence level (default 5% for CVaR).
    :return: CVaR at the given confidence level.
    """
    var = calculate_var(simulations, alpha)
    return simulations[simulations <= var].mean()

def calculate_drawdown(simulations):
    """
    Calculate the maximum drawdown (the largest peak-to-trough decline).
    :param simulations: Simulated portfolio values.
    :return: Maximum drawdown value.
    """
    return np.min(simulations / np.maximum.accumulate(simulations) - 1)