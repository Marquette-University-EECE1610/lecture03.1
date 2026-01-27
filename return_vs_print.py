def add_print(a: int, b: int) -> None:
    print(a + b)


def add_return(c: int, d: int) -> int:
    return c + d


print("Calling add_print:")
add_print(2, 3)

result = add_return(2, 3)
print("Result from add_return:", result)
