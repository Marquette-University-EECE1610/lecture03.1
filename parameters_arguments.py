def add_tax(price: int, rate: float) -> float:
    return price * (1 + rate)

total = add_tax(10, 0.055)
print(total)
