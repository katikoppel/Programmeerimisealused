"""
Ask input of numbers for 10 times and return their sum.

Ask for input until no numbers are added.
"""


def sum_ten():
    total = 0
    for i in range(10):
        num = int(input("Sisesta number: "))
        total += num
    return total


def sum_ten_while():
    counter = 0
    total = 0
    while counter < 10:
        counter += 1
        user_number = int(input(f"Sisesta {counter}. täisarv: "))
        total += user_number
    print(f"Sisestatud arvude summa on {total}")


def number_sum():
    counter = 0
    total = 0
    while True:
        counter += 1
        user_input = input(f"Sisesta {counter}. number: ")
        if user_input == "":
            break
        user_number = int(user_input)
        total += user_number
    print(f"Sisestatud {counter - 1} arvude summa on {total}")


if __name__ == '__main__':
    print(number_sum())
