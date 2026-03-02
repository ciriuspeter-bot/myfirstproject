import math
class Figure:
    def __init__(self, color):
        self.color = color
    def area(self):
        raise NotImplementedError("Low class implement")
    def round(self):
        raise NotImplementedError("Low class implement")

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def round(self):
        return 2 * math.pi * self.radius

class Rectangle(Figure):
    def __init__(self, color, row, column):
        super().__init__(color)
        self.row = row
        self.column = column
    def area(self):
        return self.row * self.column
    def round(self):
        return 2*(self.row+self.column)

a = Circle("red", 4)
b = Rectangle("blue", 15, 10)

print(f"circle : {a.area():.2f},\t {a.round():.2f}")
print(f"rectangle : {b.area()},\t {b.round()}")
        
    