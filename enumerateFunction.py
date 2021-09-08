#enumerate function adds counter to an iterable and returns it.

list_0= ["apple",50,"Orange",True,99.99]

#traditioanl approach

#index= 0
print("item: index")

'''
for i in list_0:
    print(f"{i}: {index}")
    index+=1 #equivalent to index++ in java
'''

#enumerate approach
for i,item in enumerate(list_0):
    print(i, item) #prints the item of list with index
    

'''
item: index
0 apple
1 50
2 Orange
3 True
4 99.99
'''    



