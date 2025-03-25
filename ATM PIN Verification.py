#Q5.ATM PIN Verification

pin=int(input("Enter the pin"))
count=1

if(pin==1234):
    print("Access Gained!")
else:
    while(count<3):
      print("Access Denied!")
      count=count+1
      pin=int(input("Enter the pin"))

    print("Card Blocked!")

