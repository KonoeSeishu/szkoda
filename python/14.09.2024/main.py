a = 10
print(id(a))
b = 12
print(id(a) == id(b))

x = 25
xadr = id(x)

x += 1
xadr2 = id(x)

print(xadr)
print(xadr2)

listData = ['a','b','c']
listAdd = id(listData)

listData += ['d','e']
listAdd2 = id(listData)
print(listAdd)
print(listAdd2)
print(listData)

setData = {2,3,4}
setAdd = id(setData)
setData.add(5)
print(setData)
setAdd1 = id