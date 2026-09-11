"""Function Arguments and Parameters in Python.

This example illustrates the difference between positional arguments,
default parameter values, and keyword (named) arguments.
"""


def order_coffee(coffee_type: str, size: str = "Medium") -> str:
    """Prepare a coffee order message.

    Args:
        coffee_type: The kind of coffee (e.g., 'Latte', 'Flat White').
        size: Beverage size (default: 'Medium').

    Returns:
        A formatted string describing the preparation.
    """
    return f"Brewing a {size} {coffee_type}."


# 1. Positional argument: 'Latte' matches coffee_type, size uses default 'Medium'
print(order_coffee("Latte"))

# 2. Keyword arguments: Arguments can be supplied by name in any order
print(order_coffee(size="Large", coffee_type="Flat White"))
