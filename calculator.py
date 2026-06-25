"""
A simple calculator module.

This is the "application code" for the assignment. It is deliberately small
and easy to read so the focus stays on the Git / GitHub Actions workflow.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
