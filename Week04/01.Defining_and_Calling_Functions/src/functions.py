def calculate_discount(price, discount_rate=0.10):
    return price - (price * discount_rate)


print(f"Discounted price: ${calculate_discount(100)}")
