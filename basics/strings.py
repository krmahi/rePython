import os
import sys
import random

long_string = "i'll catch my breath when i rest on the floor"

# slicing 
print(long_string[0:4:2]) # string[x:y:z] x => start, y => after end, z => steps
print(long_string[-2:])
print(long_string[:-2])
print(long_string[:4]+" be the next person to achieve it")
print(long_string.capitalize()) # capitalize first letter of string
print(long_string.find('rest')) # find word in a strin (return the first index of the word)

# to check is the words are all alphabetical
print(long_string.isalpha()) # boolean value
print(long_string.isalnum()) # boolean value
print(len(long_string)) 
print(long_string.replace('floor', 'ground')) # replace a word
print(long_string.strip()) # strip white space

# **** String to list ****
print(long_string.split()) 
# using c variable notations

print("%c is my %s letter and my number %d is %.2f decimal away" % ('A', 'favorite', 10, 1.4))