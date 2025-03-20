import random
# format (new_list = [transform sequence[filter]])

''' 1 '''
a = [x for x in range(10)]
print(a)

''' 2 '''
b = [x**2 for x in a]
print(b)

''' 3 '''
c = [x for x in range(10) if x % 2 == 1]
print(c)

''' 4 '''
s = "i love 2 go 2 the store 7 times"
d = [x for x in s if x.isnumeric()]
print(d)
print(" ,".join(d))

''' 5 '''
names = ["james", "robert", "niko"]
e = [index for index, value in enumerate(names) if value == "niko"] # enumerate() -> pairs 
print(e)
print(type(str(e)))

''' 6 '''
letters = [x for x in "ABCDE"]
print(letters)
random.shuffle(letters)
print(letters)
letrs = [a for a in letters if not a == 'C'] # can also use a != 'C'
print(letrs)

''' 7 (if else) '''
L = [x if x % 2 == 0 else x * 2 for x in range(10)]
print(L)

''' 8 (nested)'''
a = [[1,2],'w']
l = [x for b in a for x in b if not x == 'w']
print(l)