#Q 19. Create a Rectangle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create a Rectangle object
rect = Rectangle(5, 3)

# Calculate area and perimeter
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
