def double(x: int) -> int:
    print("Inside double")
    return x * 2


print("Start")
value = double(4)
print("Outside double")
print(f"Returned value: {value}")
print("End")
