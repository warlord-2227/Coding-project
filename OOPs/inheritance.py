import sys 
import os 

class Animal():
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        return f"Animal sound"
    
    def info(self):
        return f"This is information about animal{self.name}"

class Dog(Animal):
    def speak(self):
        return f"{self.name} WoW WoW"


class Walker():
    def walk(self):
        return f"{self.name} is walking"

class FlyingAnimal(Animal,Walker):
    def __init__(self, name,wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def fly(self):
        return f"{self.name} is flying with {self.wingspan} meters "

dog = Dog("goku")
print(dog.speak())
eagle = FlyingAnimal("Eagle",2.5)
print(eagle.info())
print(eagle.fly())
print(eagle.walk())

        
    