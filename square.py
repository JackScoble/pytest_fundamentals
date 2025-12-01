def area_of_a_square(side: float) -> float:
	"""Calculates the area of a square

	Arguments:
		side {float} -- length of one side of the square

	Returns:
		float -- area of the square
	"""

	# Strict type checks to avoid bools and unusual numeric types
	if type(side) not in [int, float]:
		raise TypeError("Side must be a number")

	# Value checks: side must be non-negative
	if side < 0:
		raise ValueError("Side must be a positive number")

	return side * side

