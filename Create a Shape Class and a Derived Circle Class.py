#Q20. Create a Shape Class and a Derived Circle Class

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Create a Circle object
circle = Circle(5)

# Calculate the area
print(f"Circle area: {circle.area():.2f}")
