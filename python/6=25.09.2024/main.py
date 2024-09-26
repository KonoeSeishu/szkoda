data = (1,2,4,6,"test1","test2")
print(type(data))
data1=("one",)

data2="some","more","even","umbrella";
print(data2)

print(data[1])
print(data[2:])
print(data[::2])
print(data[-1])

multiple = ((1,2,3,4), ("one","two"), data)
print(multiple[1][1])
print(multiple[2][5])

data3 = (1,2,4,6,"test1","test2")
data3[3]="test"