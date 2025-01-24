class Shape:
    def calc_area(self):
        return f"Area of shape is not defined"

class Rectange(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius ** 2

rec = Rectange(10, 20)
cir = Circle(5)
sha = Shape()

print(rec.calc_area())
print(cir.calc_area())
print(sha.calc_area())