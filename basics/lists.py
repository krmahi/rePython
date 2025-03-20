import random
import sys
import os

# empty list
x = list()

list = ["juice", "potatos", "bananas", "totmatos"]
print("second item:",list[1])
list[1] = "raw potatos"
print("second item:",list[1])

# slicing
print("slicing: ", list[0:2])

# list[list[]]
event = ["wash car", "bath"]
to_do = [event, list]
print(to_do)
print([event, list])

# multi_list_indexing (to_do[1][3])
print(to_do[1][3])

list.append("onions")
print(to_do)
print(to_do[1][4])

# operations

list.insert(1, "pickle")
list.remove("pickle")
list.sort()
list.reverse()
del (list[1])
test = []
del(test)

print(to_do)

#concatination in list

to_do_list = event + list
print(to_do_list)
print(len(to_do_list))
print(max(to_do_list))
print(min(to_do_list))

# more
x = [4,3] * 3
print(x)

# list comprehension
x = [m for m in range(8)]
print(x)
y = [i//2 for i in range(100) if i > 50]
print(y)

# extend
x = [1,2,3,4]
y = ['pig', 'cow']
x.extend(y)
print(x)

# concatination
x = [1,2,3,4]
y = ['pig', 'cow']
print(x + y)

#pop
x = [1,2,3,4]
x.pop()
print(x)