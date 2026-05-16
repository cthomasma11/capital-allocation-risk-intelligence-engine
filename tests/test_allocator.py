import numpy as np

from src.allocator import compare_allocations


def test_compare_allocations_returns_sorted_results():
    np.random.seed(42)

    simulations_dict = {
        "Conservative": np.random.normal(loc=1.05, scale=0.05, size=1000),
        "Balanced": np.random.normal(loc=1.10, scale=0.10, size=1000),
        "Aggressive": np.random.normal(loc=1.20, scale=0.20, size=1000),
    }

    results = compare_allocations(simulations_dict)

    assert isinstance(results, list)
    assert len(results) == 3

    for result in results:
        assert "allocation" in result
        assert "mean" in result
        assert "var" in result
        assert "cvar" in result
        assert "drawdown" in result

    cvar_values = [result["cvar"] for result in results]

    assert cvar_values == sorted(cvar_values)