# def printData(letters,digits=30,/):
#     print(letters, digits)
    
# printData("Test", 60)


# def printData1(*,letters,digits=30):
#     print(letters, digits)

# printData1(letters="Test", digits=1)


# def printData2(float, bool, *, string, numer=30):
#     print(float, bool, string, numer)

# printData2(15.6, bool=True, string="test3", number=21)


# def printCar(brand, /, model="concept", *, year=2000, color="red"):
#     print(brand, model, year, color)

# printCar("Toyota", "Corolla", color="green", year=2025)



def maximum_2(a,b):
    if(a>b): return(a)
    elif(b>a): return(b)
    
maximum_2(2,4)
maximum_2(-2,1)

def maximum_3(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print(maximum_3(4,2,1))
print(maximum_3(-3,2,5))
        
        
        

    


