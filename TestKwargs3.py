class Person:
    def __init__(self, name='', age=None, **kwargs):
        self.name = name
        self.age = age
        self.extra_info = kwargs
        
    def summary(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Extra Info:")
        for key, value in self.extra_info.items():
            print(f" {key}:{value}")
        
class Manager(Person):
    def __init__(self, name='', age=None, team_size=None, **kwargs):
        super().__init__(name=name, age=age, **kwargs)
        self.team_size = team_size
        
class Employee(Person):
    def __init__(self, name='', age=None, salary=None, department='', **kwargs):
        super().__init__(name=name, age=age, 
                         **kwargs)
        self.salary = salary
        self.department = department
        
manager1 = Manager(name='Alex', age=35, salary=5000, department='sales', bonus=1000)
print("=== Manager ===")
manager1.summary()


employee1 = Employee(name='Grace', age=18, dob='17/09/2007', salary=2300, department='sales')
print("\n=== Employee ===")
employee1.summary()