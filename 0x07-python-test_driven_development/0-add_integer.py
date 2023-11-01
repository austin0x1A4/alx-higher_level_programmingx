def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Default is 98.

    Returns:
    int: The addition of a and b as integers.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b
