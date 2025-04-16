file = open("test.txt", "w")
file.write("test")
file.write("test\n")
file.write("test1\n")
file.write("test2\n")
file.close()

file1 = open("test.txt", "r")
lines = file1.readLines()
file1.close()

for line in lines:
    print()