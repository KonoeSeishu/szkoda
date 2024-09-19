list = ["text", 25, 25.6, "text2", 23]
print(type(list))
print(list)
print(list[::2])
list[1] = "uwu"
print(list)
del list[1]
print(list)

for data in list:
    print(data)
    

#list multi-layer
data1 = [1,2,3,4,5],["one", "two", "three"]
print(data1[2][1])
#list connect
data2 = ["Thomas", "Anna"]
data3 = ["Robert", "Kass", "Alice"]
data4 = ["Niun", "An"]

data2+data3+data4

print