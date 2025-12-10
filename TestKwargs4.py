#!/usr/bin/env python3

class Product:
    def __init__(self, name='', price=None, **kwargs):
        self.name = name
        self.price = price
        self.extra_att = kwargs
        
    def display_self(self):
        print(f"Name:{self.name}")
        print(f"Price:{self.price}")
        print(f"Extra Attribute:")
        for key, value in self.extra_att.items():
            print(f"{key}:{value}")
            
    def apply_discount(self):
        if "discount" in self.extra_att:
            discount_percent = self.extra_att['discount']
            self.price = self.price * (1 - discount_percent / 100)
            print(f"New discounted price: {self.price}")
        else:
            print(f"No discount available")
           
class Electronics(Product):
    def __init__(self, name='', price=None , warranty='', **kwargs):
        super().__init__(name=name, price=price, **kwargs)
        self.warranty = warranty
        
class Clothing(Product):
    def __init__(self, name='', price=None, size='', **kwargs):
        super().__init__(name=name, price=price, **kwargs)
        self.size = size
        
