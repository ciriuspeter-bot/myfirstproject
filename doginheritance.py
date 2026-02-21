class Dog():
    def __init__(self, dtype, name, age):
        self.dtype = dtype
        self.name = name
        self.age = age
    def training(self):
        print(self.name+", stand up!")
    def describe_personal(self):
        fullname = "The type is "+self.dtype+" "+str(self.age)+"years old."
        return fullname
class bigD(Dog):
    def __init__(self, dtype, name, age):
        super().__init__(dtype, name, age)
newdog = bigD("bull dog", "Elle", 3)
print(newdog.describe_personal())
