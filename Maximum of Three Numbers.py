#Q 15. Find the Maximum of Three Numbers

def find_max(a,b,c):
  return max(a,b,c)


num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))

max_num=find_max(num1,num2,num3)
print(f"Maximum number is: {max_num}")
