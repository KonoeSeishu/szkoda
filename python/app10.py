class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor", self.name)
        
class Employee(Person):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname
        print("Employee constructor", self.name, self.surname)
        
        
    
    





class Vehicle:
    def __init__(self, brand, yearOfProduction):
        self.brand = brand
        self.yearOfProduction = yearOfProduction
    
    def displayInfo(self):
        print(self.brand, self.yearOfProduction)
        
        
        
class Car(Vehicle):
    def __init__(self, brand, yearOfProduction, model):
        super().__init__(brand, yearOfProduction)
        self.model = model
        