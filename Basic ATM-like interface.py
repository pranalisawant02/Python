#Q3. Basic ATM-like interface

print("Welcome!!!")
balance=int(input("Enter your balance:"))

print("MENU =>\n1.Check Balance\n2.Withdraw Amount\n3.Deposit Amount\n4.Exit")
choice=int(input("Enter your choice:"))

if(choice==1):
  print("Your balance is",balance)
elif(choice==2):
  withdraw=int(input("Enter amount to withdraw:"))
  balance=balance-withdraw
  print("Your balance is",balance)
elif(choice==3):
  deposit=int(input("Enter amount to deposit:"))
  balance=balance+deposit
  print("Your balance is ",balance)
else:
  print("Thank you!!!")
