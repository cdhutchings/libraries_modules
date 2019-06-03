# Libraries

# These are standard libraries which are always included in python.
# To use them, they simply need to be imported as so...

# import random
#
# print(random.random())
# print(random.randint(1,5))



# using the following command removes the need to specify the library when calling a function
# Importing all from a library (*) can get confusing if you aren't making use off all the function from random

from random import *
import math

print(random())
print(randint(1,5))

num = 23.66

print(math.floor(num))
print(math.ceil(num))
print(math.pi)
print(math.hypot(4,3))