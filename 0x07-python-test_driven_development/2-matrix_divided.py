def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor to divide all matrix elements by.

    Returns:
    list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats, if rows have different sizes, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_cols = len(matrix[0])

    for row in matrix:
        if len(row) != num_cols:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
