import os
import sys
import random

for x in range(0, 10):
    print(x, end=" ")
print("\n")

veggies = ["tomato", "banana", "potato"]

for y in veggies:
    print(y, end=" ")
    print(y[2], end=" ")

print("\n")
for z in [1,2,3,4,5,6,7]:
    print(z, end=" ")

print("\n")
new_list = [[1,2,3,4], [11,22,33,44], [111,222,333,444]]

for x in range(0,3):
    for y in range(0,4):
        print(new_list[x][y], end=" ")

# while loop

random_number = random.randrange(0,100)
count = 1
while(random_number != 20):
    print(random_number)
    random_number = random.randrange(0,100)
    count+=1

print("found 20: ", random_number, "in ", count, "counts")
# print("found 20 in randoms")
i = 0
while (i <= 20):
    # if (i == 9):
    #     break
    if (i%2 == 0): #even
        print(i)
    elif (i == 9):
        break
    else:
        i+=1
        continue
    i+=1

# enumerate

y = [1,2,3,4,5]
for i in enumerate(y): # to print indexes
    print(i)
