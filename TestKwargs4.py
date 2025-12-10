#!/usr/bin/env python3

class Product:
    def __init__(self, name='', price='', **kwargs):
        self.name = name
        self.price = price
        self.extra_att = kwargs
        
    def display_self(self):
        print(f"Name:{self.name}")
        print(f"Price:{self.price}")
        print(f"Extra Attribute:")
        for key, value in self.extra_att.items():
            print(f"{key}:{value}")
            
class Electronics(Product):
    def __init__(self, name='', price='', warranty='', **kwargs):
        super().__init__(name=name, price=price)
        self.warranty = warranty
        
class Clothing(Product):
    def __init__(self, name='', price='', size='', **kwargs):
        super().__init__(name=name, price=price)
        self.size = size
        
