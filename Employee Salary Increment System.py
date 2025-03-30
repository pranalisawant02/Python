#Q25. Employee Salary Increment System
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self, percentage):
        self.salary *= (1 + percentage / 100)

# Create an Employee object
emp = Employee("John Doe", 5000)

# Print initial salary
print(f"Initial salary: ${emp.salary:.2f}")

# Apply a 10% raise
emp.apply_raise(10)

# Print updated salary
print(f"Updated salary: ${emp.salary:.2f}")
