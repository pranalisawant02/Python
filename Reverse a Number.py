#Q6.Reverse a Number

n=12345
rev_no=0
while(n!=0):
  digit=n%10
  rev_no=rev_no*10+digit
  n//=10
print("Reversed no. = "+ str(rev_no))
