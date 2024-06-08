class Animal:
    def speak(self):
        return NotImplementedError(f"Subclass will implement this")

class Dog(Animal):
    def speak(self):
        print("wow")
        return f"Wow wow"

class Cat(Animal):
    def speak(self):
        print("meo")
        return f"meow meow"
    
def make_speak(entity):
    entity.speak()
    
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
make_speak(dog)
make_speak(cat)
    