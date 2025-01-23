def suma(a, b):
    return a + b

print (suma(10,12))

def addToStr(string):
    string += "!"
    print("addToStr() string as: " + string)
    
string1 = "Hello"

addToStr(string1)
addToStr(string1)

print("original string1: " + string1)

def addToList(anyway):
    anyway.append(10)
    
anyway = [1,2,3]

addToList(anyway)
addToList(anyway)
addToList(anyway)

print(str(anyway))