#Q7.ATM Cash Dispensing Machine

amount=int(input("Enter the amount:"))

print("2000 notes to be given:")
print(amount//2000)
amount=amount%2000

print("500 notes to be given:")
print(amount//500)
amount=amount%500
