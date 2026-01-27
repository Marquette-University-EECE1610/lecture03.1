def add_tax(price : float, rate: float) -> float:
    return price * (1 + rate)
total = add_tax(10.00, 0.055)
print(total)
