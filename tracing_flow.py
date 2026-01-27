def double(x: int) -> int:
    print("  Enter double")
    result = x * 2
    print(f"  Exit double with {result}")
    return result


def add_five(x: int) -> int:
    print("  Enter add_five")
    result = x + 5
    print(f"  Exit add_five with {result}")
    return result


def process_number(x: int) -> int:
    print(" Enter process_number")
    doubled = double(x)
    adjusted = add_five(doubled)
    print(f" Exit process_number with {adjusted}")
    return adjusted


print("Start")
number = 4
print(f"Initial number: {number}")
value = process_number(number)
print("Outside process_number")
print(f"Returned value: {value}")
print("End")
