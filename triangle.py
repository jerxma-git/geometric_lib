def area(a, h):
	"""Calculates the area of a triangle

	Args:
		a (float): size of the triangle's side
		h (float): triangle's height measured from the provided side

	Returns:
		float: the area
	"""
	return a * h / 2

def perimeter(a, b, c):
	"""Calculates the perimeter of a triangle

	Args:
		a (float): size of the first side (any order)
		b (float): size of the second side 
		c (float): size of the third side

	Returns:
		float: the perimeter
	"""
	return a + b + c
