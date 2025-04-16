# class Person:
#     def __init__(self, name, surname, country):
#         self.name = name
#         self.surname = surname
#         self.counry = country

#     def getFullName(self):
#         return f"Full name {self.name} {self.surname}"

#     def printData(self):
#         return f"{self.name} {self.surname} {self.country}"

# per1 = Person("Ola", "Kowalska", "pl")
# per1.printData()


class Radio:
    def __init__(self, brand, frequency, volume):
        self.brand = brand
        self.frequency = frequency
        self.volume = volume
        self.isOn = False
        
    def turnOn(self):
        self.isOn = True
        
    def turnOff(self):
        self.isOn = False
        
    def getRadioInfo(self):
        return f"Marka:{self.brand}, Czestotliwosc:{self.frequency} MHz, Glosnosc:{self.volume}"
            
            
radio1 = Radio("Sony", 101.2, 5, )
print(radio1.getRadioInfo())
radio2 = Radio("Philips", 98.7, 7)
print(radio2.getRadioInfo())
        
class Book:
    def __init__(self, autor, title="none", isbn="none", year="none"):
        self.autor = autor
        self.title = title
        self.isbn = isbn
        self.year = year
        
    def printData(self):
        print(self.autor, self.title, self.isbn, self.year)
        
book1 = Book("Jan")
book1.printData()

book2 =  Book("adam mick", year=2023)
book2.printData()

book3 =  Book("nore", "bruh","DGAGA@", 2023)
book3.printData()

        
    
    
