from abc import ABC,abstractmethod

# Abstract Class 
class Animal(ABC):
    def __init__(self,name) -> None:
        self.name = name 
    
    @abstractmethod 
    def speak(self):
        pass
    
    def info(self):
        return f"Name of Animal is {self.name}"

# Subclass     
class Dog(Animal):
    def speak(self):
        return f"Wow wow"
    
class Cat(Animal):
    def speak(self):
        return f"meow meow"
    
dog = Dog("Bull")
cat = Cat("Whiskers")

#using method of subclass and abstract class
print(dog.speak())
print(dog.info())
print(cat.speak())
print(cat.info())
