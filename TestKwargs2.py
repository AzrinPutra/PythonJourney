
class Vehicle:
    def __init__(self, make='', model='', **kwargs):
        self.make = make
        self.model = model
        self.extra_attributes = kwargs
        
class Car(Vehicle):
    def __init__(self, make='', model='', doors=None, **kwargs):
        super().__init__(make=make, model=model, **kwargs)
        self.doors = doors
        
class Truck(Vehicle):
    def __init__(self, make='', model='', capacity=None, **kwargs):
        super().__init__(make=make, model=model, **kwargs)
        self.capacity = capacity
        
car1 = Car(make='Honda', model='Civic', doors=5, year=1992)
truck1 = Truck(make='Toyota', model='HiAce', capacity=2000, color='Grey')

print("Car1:", vars(car1))
print("Truck1:", vars(truck1))

print("Car1 extra:", car1.extra_attributes)
print("Truck1 extra:", truck1.extra_attributes)