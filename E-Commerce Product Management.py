#Q23. E-Commerce Product Management

class Product:
  def __init__(self, name, price,stock):
    self.name=name
    self.price=price
    self.stock=stock

  def purchase(self,quantity):
    if self.stock>=quantity:
      self.stock-=quantity
      print(f"Purchased { quantity } {self.name}s.Remaining stock:{self.stock}")

    else:
      print("Insufficient stock!")

product=Product("Apple Watch",2999,10)

product.purchase(2)
product.purchase(15)

