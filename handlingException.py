
try:
     a= int(input("Please enter a number not equals to zero: "))
     print(45/a)
except ZeroDivisionError as e:
    print(f"You fucking asshole entered zero.")
    print(e)
except ValueError as e:
    print("You fucker didn't enter any number") 
    print(e)   
