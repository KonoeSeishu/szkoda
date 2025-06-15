class Vehicle:
    def __init__(self):
        self.__gears = 5
        
    def gears(self):
        if(self.__gears >0):
            return self.__gears
        else:
            return -1
        
    def printGears(self):
        print("Gears:", self.__gears)
        
Vehicle1 = Vehicle()
Vehicle1.gears = 7
Vehicle1.printGears()
        
        
        