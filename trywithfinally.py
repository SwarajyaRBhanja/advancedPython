
#try with finally: python offers a finally clause which ensures execution of a piece of code irrespective of an exception

try:
    x= int(input("Enter a number: "))
    print(25/x)
except ValueError:
    print("The entered value is not a number")
    exit()
except ZeroDivisionError:
    print("The entered value is zero")
    exit()
else:
    print("I am being executed as your try block is successful")
finally:
    print("I will always be executed, don't give a fuck whether you got any error or not")        

print("I will not be printed if you have got any exception")            