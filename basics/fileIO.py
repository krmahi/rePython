import os
import sys
import random

file = open("test.txt", 'wb')

# informations
print(file.mode)
print(file.name)

file.write(bytes("write this to the file\n",'UTF-8'))
file = open("test.txt", 'r+')
content = file.read()
print(content)
file.close()

os.remove("test.txt")