
#Write a program to print third, fifth & seventh element from a list using enumerate function.

l1= [3,4,5,7,9,0,12,45,78]

print("index element_position element_value")
for index,item in enumerate(l1):
    if(index==2 or index==4 or index==6):
        print(index,index+1, item)

    
    
