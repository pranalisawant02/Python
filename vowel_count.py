str=input("Enter the string:")

count=0

for i in range(len(str)):
    if str[i] in ['a','A','e','E','i','I','o','O','u','U']:
        count+=1

print(f"The count of vowels in a string is:{count}")
