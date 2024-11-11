def subtract(a, b):
    return a - b


def sum(a, b):
    """
    >>> sum(1, 2)
    3

    >>> sum(3, -4)
    -1
    """
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: Division by zero is not allowed
    """

    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
