from functools import reduce

sum= lambda x,y: x+y
l1= [4,8,4,9,7]

print(reduce(sum,l1)) #32

#reduce applies a rolling computation to sequential pair of elements

