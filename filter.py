
#filter creates a list of items for which the fucntion returns true, function can be a lambda function

#syntax: list(filter(function,l))

greater_than_5= lambda x:x>5

l1=[4,5,6,8,9,5,3,6,8,34,5,7]
print(list(filter(greater_than_5,l1)))
