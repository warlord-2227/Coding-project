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


dog = Dog("goku")
print(dog.speak())
        
    