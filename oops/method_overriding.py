"""
Method Overriding means defining the attributes in the parent class but, implementing them in the child classes.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """In method overriding, the parent class defines the structure of the child classes."""
    def __init__(self, species: str) -> None:
        self.species = species

    @abstractmethod
    def greet(self):
        """This method has to be implemented by child classes."""
        pass

class Dog(Animal):
    def greet(self):
        print("Woof!")

class Cat(Animal):
    def greet(self):
        print("Meow!")

if __name__ == "__main__":
    dog = Dog('Dog')
    cat = Cat('Cat')
    dog.greet()
    cat.greet()