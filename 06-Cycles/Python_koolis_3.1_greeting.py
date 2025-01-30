def greet_name():
    """Greet the user's name 5 times."""
    name = input("Sisesta oma nimi: ")
    for i in range(5):
        print(f"Ole tervitatud, {name}, {i + 1}. korda!")


if __name__ == '__main__':
    greet_name()
