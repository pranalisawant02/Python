#Q1. Identify the Employee Category

salary=int(input("Enter employee salary:"))

if(salary>50000):
  print("High Income.")
elif(salary>30000 and salary<50000):
  print("Medium Income.")
else:
  print("Low Income.")
