def order_coffee(type, size="Medium"):
    return f"Brewing a {size} {type}."


print(order_coffee("Latte"))
print(order_coffee(size="Large", type="Flat White"))
