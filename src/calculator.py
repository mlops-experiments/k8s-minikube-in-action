# write basic calculator functions
def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def power(x, y):
    """Return x raised to the power of y."""
    return x ** y


# extend basic calculator functions
# Function to square
def square(n):
    return n ** 2


# Function to cube
def cube(n):
    return n ** 3


# Function to fifth power
def fifth_power(n):
    return n ** 5
