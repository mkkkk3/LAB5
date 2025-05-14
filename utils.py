# Exemplary calculator functions

"""
Module: utils
Contains basic calculator functions for addition, subtraction, multiplication, and division.
"""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the result of dividing a by b."""
    return a / b


def to_binary(n: int) -> str:
    """
    Convert a natural number from 0 to 100 to a binary string.
    Raises:
        ValueError: If the input is not a natural number in range 0–100.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0 or n > 100:
        raise ValueError("Input must be between 0 and 100.")
    return bin(n)[2:]
