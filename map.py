
#map applies a function to all the items in an input list.
#syntax: map(function, input_list), can be lambda function

#traditional methos


def squere(n):
    return n*n
'''
l1= [4,7,8]
l2= []

for item in l1:
    l2.append(squere(item))
print(l2)
'''
print(list(map(squere,[4,7,9]))) #[16, 49, 81]