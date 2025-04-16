#files + UTF-8

import os

script_dir = os.path.dirname(__file__)
print(script_dir)

file_path = open(script_dir+"/og.txt","w",encoding="UTF-8")
file_path.write("lub")
file_path.close()
