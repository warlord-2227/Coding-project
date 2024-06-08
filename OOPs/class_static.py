class MyClass:
    count = 0 
    def __init__(self) -> None:
        pass
    @classmethod
    def increment_count(cls):
        cls.count += 1 
        
MyClass.increment_count()
print(MyClass.count)
MyClass.increment_count()
print(MyClass.count)
clt = MyClass()
clt.increment_count()
print(clt.count)

