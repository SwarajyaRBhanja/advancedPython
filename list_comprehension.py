a= [2,4,7,8,9,23,54,61,72,18]

#tradition approach
'''
b= []
for i in a:
    if i%2==0:
        b.append(i)
'''
b=[i for i in a if i%2==0]
print(b)
 
#list comprehension is an elegant way to create list based on existing list.

c=[k for k in a if k>20] 
print(c)

x= [3,5,6,8,4,12,4,7,8,3,7,8]
print({y for y in x}) #printing a set {3, 4, 5, 6, 7, 8, 12}
