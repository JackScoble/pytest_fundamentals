from math import pi


def area_of_a_circle(radius: float) -> float:
    """Calculates the area of a circle

    Arguments:
        radius {float} -- radius of the circle

    Returns:
        float -- area of the circle
    """

    # Type checks are intentionally strict: only int or float are accepted
    if type(radius) not in [int, float]:
        raise TypeError("Radius must be a number")

    # Value checks: radius must be non-negative
    if radius < 0:
        raise ValueError("Radius must be a positive number")

    return pi * (radius ** 2)
