"""Trading pipeline."""
from .get import get_stock_data
from .plot import plot_stock_data


def run():
    """Run trading pipeline."""
    # Get data
    data = get_stock_data()

    # Visualize data
    plot_stock_data(data)

    # Preprocess data

    # Create model

    # Train model

    # Evaluate model

    # Save model

    # Make predictions

    # Visualize predictions

    # Save predictions

    return data
