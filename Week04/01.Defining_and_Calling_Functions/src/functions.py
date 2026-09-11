"""Defining and Calling Functions in Python.

This example demonstrates how to define a function with a default parameter
and return a calculated value.
"""


def calculate_discount(price: float, discount_rate: float = 0.10) -> float:
    """Calculate the final price of an item after applying a discount rate.

    Args:
        price: The original price of the item.
        discount_rate: The discount fraction (default is 0.10 for 10% off).

    Returns:
        The discounted price.
    """
    return price - (price * discount_rate)


# Call function using the default 10% discount rate
original_price = 100
discounted = calculate_discount(original_price)
print(f"Discounted price: ${discounted}")
