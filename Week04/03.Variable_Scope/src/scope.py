"""Variable Scope Demonstration in Python.

This script demonstrates local variable scope: variables defined inside
a function are local to that function and must be returned to be used outside.
"""


def update_balance() -> int:
    """Simulate updating an account balance.

    Returns:
        The updated account balance.
    """
    # 'balance' is a local variable scoped exclusively to this function
    balance = 500
    return balance


# Capture the returned value in global scope
my_balance = update_balance()
print(f"My balance is: ${my_balance}")
