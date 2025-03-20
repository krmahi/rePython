import sys
import random

print(2/3)
print(2*3)
print(2+3)
print(2-3)
print(2//3)
print(2**3)

quote = "\"always remember"
print(quote)

multi_line_quote = ''' u have
yourself| '''
print(multi_line_quote)

# concatination

new_string = quote + multi_line_quote
print(new_string)

# %s print for instead of concatination

print("%s %s %s" % ("quote = ", quote, multi_line_quote))

print("i don't like", end = "")
print(" govt.")

# newline ('\n')

# print("\n" *5)

# sum
y = [1,2,3,4,5]
print(sum(y))
print(sum(y[:-1]))

# sorted
y = [1,2,5,4]
print(sorted(y))

# count
y = 'pigg'
print(y.count('g'))

# index
y = 'piggg'
print(y.index('g'))

# unpack
y = [1 , 2, 3, 4]
a,b,c,d = y
print(a,b,c)