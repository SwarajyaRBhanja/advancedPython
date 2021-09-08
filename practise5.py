
from functools import reduce

l= [5,6,7,8,9,4,3,56,8,9,12,45,3,4,67,8,9]

a= reduce(max,l)
print(a)
