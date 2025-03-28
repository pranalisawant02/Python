#Q16. Create a Student Class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40

student1 = Student("John", 75)
student2 = Student("Jane", 30)

print(f"{student1.name} passed: {student1.has_passed()}")
print(f"{student2.name} passed: {student2.has_passed()}")
