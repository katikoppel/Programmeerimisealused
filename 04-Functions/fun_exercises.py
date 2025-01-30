"""Function examples."""


def func():
    """Print to console - I am inside the function."""
    print("I´m inside the function")


def my_name_is(name: str) -> None:
    """Print to console - my name is [name].

    :param name: name You want to use
    """
    print(f'My name is {name}')


def sum_six(num: int) -> int:
    """Return sum of six and input argument."""
    return (int(num) + 6)


def sum_numbers(num_a: int, num_b: int) -> int:
    """Return sum of num_a and num_b input argument."""
    return num_a + num_b


def usd_to_eur(num: int) -> None:
    """Calculate input in USD to Euro."""
    return (float(num * 80 / 100))


"""Test the functions."""
if __name__ == '__main__':
    print(func())
    print(my_name_is("kati"))
    print(sum_six(2))
    print(sum_numbers(2, 3))
    print(usd_to_eur(55))
