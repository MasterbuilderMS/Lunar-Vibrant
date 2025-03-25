import math  # Import statement

# Global variables
PI = 3.14159
greeting = "Hello, World!"
numbers = [1, 2, 3, 4, 5]

# Decorator function


def log_function_call(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Class definition


class Shape:
    """A simple Shape class"""

    # Class variable
    shape_count = 0

    def __init__(self, name: str, sides: int):
        """Constructor"""
        self.name = name
        self.sides = sides
        Shape.shape_count += 1

    @staticmethod
    def info():
        """Static method"""
        return "Shapes have sides!"

    @log_function_call
    def area(self):
        """Method to calculate area (dummy implementation)"""
        return self.sides * 10

# Inheritance


class Circle(Shape):
    """Circle class inherits from Shape"""

    def __init__(self, radius: float):
        super().__init__("Circle", 1)
        self.radius = radius

    @log_function_call
    def area(self) -> float:
        """Overrides area method"""
        return PI * self.radius ** 2


# Lambda function
def square(x): return x * x


# Dictionary comprehension
squared_numbers = {x: x ** 2 for x in numbers}

# Function with multiple elements


@log_function_call
def calculate_distance(x: float, y: float) -> float:
    """Calculates the Euclidean distance from origin"""
    return math.sqrt(x**2 + y**2)


# Main script execution
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Circle Area: {circle.area()}")

    shape = Shape("Triangle", 3)
    print(f"Shape Area: {shape.area()}")

    print(f"Squared Numbers: {squared_numbers}")
    print(f"Distance: {calculate_distance(3, 4)}")
