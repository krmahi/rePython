import os
import sys
import random

# creation
x = ()
x = (1,2,3)
x = 1,2,3
x = 1, # this is also a tuple

new_tuple = (1,2,3,4,5)
print(new_tuple)
convert_tuple = list(new_tuple)
convert_tuple.append(6)
del convert_tuple[1]
changed_tuple = tuple(convert_tuple)
print(changed_tuple)

# more
x = (4,3) * 3
print(x)

# mutable elements
x = ([1,3],5)
del(x[0][1])
print(x)

#concatinating tuples
print(x + (4,))