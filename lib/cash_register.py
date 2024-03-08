#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0) -> None:
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    
    for i in range(quantity):
      self.items.append(title)
      self.total += price * quantity
      
    self.last_transaction = {
      'title': title,
      'price':price,
      'quantity': quantity
    }

  def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")
  
  def void_last_transaction(self):
        if self.items:
            last_price = self.total - (price for price in reversed(self.items) if price != self.total).__next__()
            self.total -= last_price
            self.items = self.items[:-1]
        else:
            print("No transactions to void.")

