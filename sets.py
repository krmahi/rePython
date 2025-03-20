# non duplicate
# fast access
# union and intersection op
# unordered sets

test = {1,2,3,4}
print(test)

set2 = set() #empty
print(set2)

list = [1,2,3,4]
list_set = set(list)
print(list_set)

# set operations
x = {1,2,3}

x.add(7)
print(x)

x.remove(2)
print(x)

print(x.pop(), x) # pops out random item from set

print(5 in x) # boolean

x.clear() # delete all items in set

# mathematical operations
x = {1,2,3,4}
y = {3,4}

print(x & y) # AND (intersection)
print(x | y) # OR (union)
print(x ^ y) # XOR (symmetric difference)
print(x - y) # difference
print(x <= y) # x subset of y
print(x >= y) # x superset of y or y subset of x


