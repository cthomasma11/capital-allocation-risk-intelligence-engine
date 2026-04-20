import numpy as np
import pandas as pd

class MonteCarloSimulator:
    def __init__(self, assets, returns_df, num_simulations=1000, horizon=252):
        """
        Initialize the simulator with assets, returns, number of simulations, and time horizon.
        :param assets: List of asset names.
        :param returns_df: DataFrame with historical returns for each asset.
        :param num_simulations: Number of Monte Carlo simulations to run.
        :param horizon: Number of days to simulate (usually 252 for 1 year).
        """
        self.assets = assets
        self.returns = returns_df
        self.num_simulations = num_simulations
        self.horizon = horizon
    
    def simulate_portfolio(self, weights):
        """
        Simulate the portfolio value over time for given asset weights.
        :param weights: List of portfolio weights for the assets.
        :return: A list of simulated final portfolio values.
        """
        simulations = []
        for _ in range(self.num_simulations):
            daily_returns = np.random.choice(self.returns[self.assets].values.flatten(), 
                                             size=(self.horizon, len(self.assets)))
            portfolio_returns = np.dot(daily_returns, weights)
            portfolio_cum = np.cumprod(1 + portfolio_returns)  # Cumulative product of returns
            simulations.append(portfolio_cum[-1])  # Final portfolio value after all days
        return np.array(simulations)