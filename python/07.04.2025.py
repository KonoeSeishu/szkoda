class vehicle:

    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 150
        self.numWheels = 4
    
    def printVehicleInfo(self):
        print(self.brand, self.name, self.topSpeed)

class Car(vehicle):
    def printCarInfo(self):
        self.band = "Ford"
        self.name = "Mustang"
        print("Car brand", self.band)
        print("Car name", self.name)
        
    
    def printVehicleInfo(self):
        print("Car.printVehicleInfo:", self.brand, self.name, self.topSpeed)
    
    
class superCar(Car):
    def reachSpeed(self):
        self.topSpeed = 300
        print("Super car reached 300!")
        
        
vehicle1 = vehicle("Vehicle", "basic") 
vehicle1.printVehicleInfo
        
car1 = Car("Toyota", "Corolla")
car1.printCarInfo
car1.printVehicleInfo

superCar1 = superCar("Ford", "GT")
superCar1.reachSpeed
superCar1.printVehicleInfo


