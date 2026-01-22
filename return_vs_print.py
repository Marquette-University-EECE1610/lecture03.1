def add_print(a: int, b: int) -> None:
    print(a + b)


def add_return(a: int, b: int) -> int:
    return a + b


print("Calling add_print:")
add_print(2, 3)

result = add_return(2, 3)
print("Result from add_return:", result)
