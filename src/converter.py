"""Temperature conversion helpers."""

from numbers import Real


def _validate_temperature(value: Real) -> None:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError("temperature must be a real number")


def celsius_to_fahrenheit(celsius: Real) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    _validate_temperature(celsius)
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: Real) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    _validate_temperature(fahrenheit)
    return (fahrenheit - 32) * 5 / 9
