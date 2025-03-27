#Q13. Student Grade Calculator

def calculate_grades(marks):

  if(marks>=90 and marks<=100):
    return "A"
  elif(marks>=80 and marks<=89):
    return "B"
  elif(marks>=70 and marks<=79):
     return "C"
  elif(marks>=60 and marks<=69):
     return "D"
  else:
    return "Fail!"

marks=float(input("Enter the marks:"))
grades=calculate_grades(marks)
print(f"Student Grades: {grades}")
