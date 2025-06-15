# z1
def minutyNaSekundy(liczba_minut):
    return (liczba_minut*60)

print(minutyNaSekundy(100))

# z2
def extractionUniqueElements(inputList):
    newlist=[]
    inputList=set(inputList)
    
    for i in inputList:
        if i in newlist:
            continue
        else:
            newlist.append(i)
    return(newlist)

print(extractionUniqueElements(["nya", "nope", "nope", "yes"]))

# z3
def ElementsReverse(inputList):
    newlist=[]
    for i in inputList:
        newlist.insert(0,i)
    return(newlist)

print(ElementsReverse([6,6,6,6,4,3,3,2,1]))

# z4
def findLongestWord(sentence):
    LongestWord = ""
    CurrentWord = ""

    for i in sentence:
        if i == "" or i=="," or i==".":
            if len(LongestWord)< len(CurrentWord):
                LongestWord=CurrentWord
            CurrentWord = ""
        else:
            CurrentWord = CurrentWord + i
    return(LongestWord)

print(findLongestWord("Something, nya, nya, nya."))

# z5
def calculateAverage(numbers):
    numbersLenght = len(numbers)
    numbersSum = 0
    if not numbers:
        return 0
    for i in numbers:
        numbersSum=numbersSum+i   
    return(numbersSum/numbersLenght)
        
print(calculateAverage([1,2,6,8,2]))

# z6
def calculatePower(base, exponent):
    pass