floatNumber = 15.6
print(type(floatNumber))

intNumber = int(floatNumber)
print(intNumber)
print(type(intNumber))

x = 5 
print(type(x))
y = '12'
z = int('15')
print(type(y))
print(type(z))

floatNumber1 = float(z)
print(type(floatNumber1))
print(floatNumber1)

floatNumber2 = float("123.56")
print(type(floatNumber2))
print(floatNumber2)

data = 254
strData = str(data)
print(type(strData))
print(strData)
dataFloat = 545.78
strData1 = str(dataFloat)
print(type(strData1))

listData = [1,2,3,4]
print(type(listData))
tupleData = tuple(listData)
print(type(tupleData))

tupleData1 = ("one", "two")
print(type(tupleData1))
newList = list(tupleData1)
print(type(newList))

listaData = [1,2,2,3,3,3,4,5,6,7,7]
setData = set(listaData)
print(type(setData))

frozensetData = frozenset(listaData)
print(type(frozensetData))

tupleData2 =  (("one", "two", "snow","something"))
dictData = dict(tupleData)
print(type(dictData))
print(dictData)


print(bool())
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool((1,2,3,4)))
print(bool([]))
print(bool(""))
print(bool(True))
print(bool(-10))
print(bool("nya"))
print(bool([0]))
print(bool(1))

logData = None
print(type(logData))

if logData is True:
    print("logData is true")
elif logData is False:
    print("logData is false")
else:
    print("logData is None")


