# Portfolio Risk Simulation Engine

A **quantitative finance project** that simulates portfolio performance under uncertainty and identifies optimal allocation strategies using risk-adjusted metrics. The engine is built using **Monte Carlo simulation** and incorporates **downside risk metrics** like **VaR**, **CVaR**, and **maximum drawdown**.

## 🚀 Objective

Evaluate portfolio allocation strategies under uncertainty and recommend an optimal allocation based on **risk-adjusted returns** using real market data (Apple and Microsoft).

## ⚙️ Methodology

- **Monte Carlo simulation** of portfolio returns (100–10,000 trials)
- Bootstrapped sampling of asset return distributions
- Risk metrics:
  - **Value at Risk (VaR)**
  - **Conditional Value at Risk (CVaR)**
  - **Maximum Drawdown**
- Comparative analysis of multiple portfolio strategies

## 📈 Key Outputs

- Simulated portfolio paths to visualize uncertainty over time
- Distribution of outcomes with **VaR** and **CVaR** thresholds
- **Drawdown analysis** to evaluate worst-case losses
- **Risk vs return tradeoff visualization** across portfolios

## 🧠 Key Insight

The **Balanced portfolio** was dominated, exhibiting higher downside risk than the **Aggressive portfolio** while delivering lower expected returns.

## ✅ Recommendation

The **Aggressive portfolio** provided the strongest risk-return tradeoff, maximizing expected value without proportionally increasing downside risk.

## 📁 Project Structure

```text
capital-allocation-risk-engine/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 03_monte_carlo_simulation.ipynb
│   ├── 04_risk_metrics.ipynb
│   ├── 05_allocation_comparison.ipynb
│   └── 06_decision_summary.ipynb
├── src/
│   ├── simulator.py
│   ├── risk_metrics.py
│   ├── allocator.py
├── reports/
│   └── charts/
│       ├── simulated_paths.png
│       ├── var_cvar_chart.png
│       ├── drawdown_chart.png
│       └── allocation_frontier.png
├── streamlit_app.py
└── LICENSE
