# Using map() with a lambda function to double the prices
prices = [10.0, 25.0, 50.0]

# map() applies the lambda function to each element in the prices list
doubled_prices = list(map(lambda x: x * 2, prices))

# Print the doubled prices
print(doubled_prices)


# Alternative using a regular function
def double_price(price):
    return price * 2
printed_prices = list(map(double_price, prices))
print(printed_prices)