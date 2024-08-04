class MyCustomError(Exception):
    """This is a custom exception class."""
    pass

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
    raise MyCustomError("This is a custom error message.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except MyCustomError as e:
    print(e)