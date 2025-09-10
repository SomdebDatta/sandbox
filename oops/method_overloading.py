"""
Method Overloading means 2 or more functions having the same name but different arguments.
Python doesn't support this kind of method overloading, if you define, multiple methods with the same name, only the latest one will be implemented.
"""

def greet() -> None:
    """Greets once."""
    print("Hello World!")

def greet() -> None:
    """Greets twice."""
    print("Hello World!!")
    print("Hello again!")

# Python does allow operator overloading

class Sample:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def coords(self) -> tuple[int, int]:
        return self.x, self.y

    def __add__(self, other) -> tuple[int, int]:
        """Operator overloading for built-in operators
        You can also overload other built-in operators like __str__, __gt__, __ge__"""
        return self.x + other.x, self.y + other.y



if __name__ == "__main__":
    greet()
    point1 = Sample(1, 2)
    point2 = Sample(2, 3)
    print(point1 + point2)
