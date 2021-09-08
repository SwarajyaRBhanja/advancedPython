#raising exception: we can raise custom exception using the raise keyword in python
'''
def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good Swarajya.") 
a= increment("a")
print(a)  

'''

#try with else clause
#sometimes we want to run a piece of code when try is sucessful, the code within else will only be executed if try is successful

try:
    i= int(input("Enter a number: "))
    print(1/i)
except Exception as e:
    print(e)
else:
    print("Inside else block, I am being executed as your try block is successful")        

