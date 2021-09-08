#write a list comprehension to print a list which contains the multiplication table of a user entered number and store it in a table

x= int(input("Please enter a number: "))

y=[x*i for i in range(1,11)]
print(y) 

with open("/Users/swarajyabhanja/Desktop/Python/advancedPython/1.txt",'w') as f:
    f.write(str([x*i for i in range(1,11)]))
    f.write("\n")
  
    
