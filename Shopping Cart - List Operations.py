#Q8.Shopping Cart - List Operations
cart = []

while True:
    item = input("Enter item ('done' to finish): ")
    if item.lower() == 'done':
        break
    cart.append(item)

print("Your cart:", cart)
