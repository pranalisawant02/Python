#Q14. Simple Calculator Using Functions

def calculator(num1,num2,operator):

  if(operator=='+'):
    sum=num1+num2
    return sum
  elif(operator=='-'):
    diff=num1-num2
    return diff
  elif(operator=='*'):
    product=num1*num2
    return  product
  elif(operator=='/'):
    if(num2!=0):
      div=num1/num2
      return div
    else:
      return "ERROR! Div by zero"

num1=float(input("Enter the 1st number:"))
operator=input("Enter the operator to perform the operation: (+,-,*,/)")
num2=float(input("Enter the 2nd number:"))

result=calculator(num1,num2,operator)
print(f"Result = {result}")

