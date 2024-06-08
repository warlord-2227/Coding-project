class Animal:
    def speak(self):
        return NotImplementedError(f"Subclass will implement this")

class Dog(Animal):
    def speak(self):
        return f"Wow wow"

class Cat(Animal):
    def speak(self):
        return f"meow meow"
dog =Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

    