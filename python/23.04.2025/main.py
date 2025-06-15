#files + UTF-8

import os

script_dir = os.path.dirname(__file__)
print(script_dir)

file_path = open(script_dir+"/og.txt", "w", encoding="UTF-8")
file_path.write("lub")
file_path.close()

file_read = open(script_dir+"/og.txt", "r", encoding="UTF-8")
lines = file_read.readlines()
file_read.close()

for line in lines:
    print(line)
    
    
    
#binary in files

import pickle

script_dir = os.path.dirname(__file__)

num1 = 12345
string1 = "TEST"
list1 = ["YEP","NO","MBY","IDK"]
