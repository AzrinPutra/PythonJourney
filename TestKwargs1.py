class Property:
    def __init__(self, square_feet=None, beds=None, baths=None, **kwargs):
        if square_feet is not None:
            self.square_feet = square_feet
        if beds is not None:
            self.beds = beds
        if baths is not None:
            self.baths = baths
        self.extra_attributes = kwargs
        
    def display_extra_att(self):
        if self.extra_attributes:
            for key, value in self.extra_attributes.items():
                # .items() → gives (key, value) pairs from the dictionary.
                # so self.extra_attributes is a dictionary
                print(f"{key}:{value}")
        else:
            print("No extra attributes")