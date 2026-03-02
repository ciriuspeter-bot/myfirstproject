class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Hi, {self.name}!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
d1 = Dog("Rex")
d1.speak()