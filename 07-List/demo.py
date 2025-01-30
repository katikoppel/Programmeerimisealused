def decrement_all(numbers: list):
    result = numbers[::]
    for i in range(len(numbers)):
        numbers[i] -= 1
    return result


numbers = [1, 2, 3]
print(f"{numbers=}")
decremented_numbers = decrement_all(numbers)
print(f"decremented {numbers=}")

names = ["ago", "mati", "reinuvader", "kasparr", "guido"]
print(min(names, key=lambda x: x[::-1]))


def reverse_lower(name):
    return name[::-1]
