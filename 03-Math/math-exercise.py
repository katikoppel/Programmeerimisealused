"""Math exercise."""

import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b  # Perform float division
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b  # Perform integer division
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b, and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2  # Calculate the average
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * (radius ** 2)  # Calculate the area using πr²
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> float:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = (math.sqrt(3) / 4) * (side_length ** 2)  # Area formula for an equilateral triangle
    return round(triangle_area)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = (b ** 2) - (4 * a * c)  # Discriminant formula
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a**2 + b**2)  # Use Pythagoras' theorem to calculate the hypotenuse
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c**2 - a**2)  # Use Pythagoras' theorem to calculate the missing cathetus
    return b


if __name__ == "__main__":
    assert sum_and_difference(5, 6) == (11, -1)
    assert sum_and_difference(11, 9) == (20, 2)
    assert sum_and_difference(9, 3) == (12, 6)
    assert sum_and_difference(20, 3) == (23, 17)
    assert round(float_division(num_a=20, num_b=3), 2) == 6.67  # Corrected syntax

    assert integer_division(num_a=10, num_b=3) == 3
    assert integer_division(num_a=7, num_b=11) == 0

    assert powerful_operations(num_a=10, num_b=3) == (30, 1000, 1)
    assert powerful_operations(num_a=2, num_b=10) == (20, 1024, 2)

    assert find_average(num_a=3, num_b=7) == 5.0
    assert find_average(num_a=999, num_b=999) == 999.0

    assert round(area_of_a_circle(1), 2) == 3.14
    assert round(area_of_a_circle(19), 2) == 1134.11

    assert round(area_of_an_equilateral_triangle(3), 2) == 3.90

    print("OK")
