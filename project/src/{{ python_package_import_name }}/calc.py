import numpy as np


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def subtract_numbers(a: int, b: int) -> int:
    """
    Subtract one number from another.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of subtracting b from a.
    """
    return a - b


def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b


def divide_numbers(a: int, b: int) -> float:
    """
    Divide one number by another.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of dividing a by b.
    """
    return a / b


def average_numbers(numbers: list[int]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list[int]): The list of numbers.

    Returns:
        float: The average of the numbers.
    """
    return np.average(numbers)
