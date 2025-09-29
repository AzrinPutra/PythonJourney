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
    valid_balconies=("yes", "no", "solarium")
    valid_laundries=("coin", "ensuite", "none")
    
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        
    def display(self):
        super().display()
        print("Apartment Details")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))
        
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = ''
        
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilites does the property have? ({})".format(\
                ", ".join(Apartment.valid_laundries)))
        
        balcony = ''
        
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? ({})".format(\
                ", ".join(Apartment.valid_balconies)))
            
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        
        return parent_init
    
    prompt_init = staticmethod(prompt_init)
    
        
    
    