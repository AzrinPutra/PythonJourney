#!/usr/env/bin python3

class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths
        
    def display(self):
        print("PROPERTY DETAILS")
        print("=========================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.beds))
        print("bathrooms: {}".format(self.baths))
        
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),\
            beds=input("Enter number of bedrooms: "),\
                baths=input("Enter number of bathrooms: "))
        
    prompt_init = staticmethod(prompt_init)
    

class Apartment(Property):
    # input validation for later
    valid_balcony=("yes", "no", "solarium")
    valid_laundry=("coin", "ensuite", "none")
    
    def __init__
    
    
    
    