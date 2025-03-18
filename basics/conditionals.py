import os
import sys
import random

age = 20
# if age <= 16:
#     print("under age")
# else:
#     print("right age")

if age >= 21:
    print("can drive commercial vehicles")
elif age > 16:
    print("can drive road vehicles")
else:
    print("not legal to drive vehicle")

# logical  operators
# and, or, not
if((age > 10) and (age == 20)):
    print("birthday")
elif ((age > 20 ) or (age == 65)):
    print("go work")
elif not(age == 30):
    print("be 30")
else:
    print("rest")