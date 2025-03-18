import os
import sys
import random

# dict = {key:value}

new_dict = {1:'A', 
            2:'B',
            3:'C'}
print(new_dict)
print(new_dict[3])

# operations
# del new_dict[1]
new_dict[2] = 'D'
new_dict[4] = 'E' #add
print(new_dict)
print(len(new_dict))
print(new_dict.get(4))
print(new_dict.keys())
print(new_dict.values())
