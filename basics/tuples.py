import os
import sys
import random

new_tuple = (1,2,3,4,5)
print(new_tuple)
convert_tuple = list(new_tuple)
convert_tuple.append(6)
del convert_tuple[1]
changed_tuple = tuple(convert_tuple)
print(changed_tuple)
