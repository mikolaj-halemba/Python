import itertools as it
import math


notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
temp = 0
for x in it.combinations(notes,4):
    temp += 1
    print(x)
print(temp)

temp = 0
for x in it.combinations_with_replacement(notes,4):
    temp += 1
    print(x)
print(temp)

