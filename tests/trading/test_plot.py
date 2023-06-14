"""Tests for src/trading/plot.py."""
from src.trading.get import get_stock_data
from src.trading.pipeline import run
from src.trading.plot import plot_stock_data


def test_plot_stock_data():
    """It plots stock data."""
    data = get_stock_data()
    plot_stock_data(data)
    assert True


def test_pipeline():
    """It runs the pipeline."""
    run()
    assert True
