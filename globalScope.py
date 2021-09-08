a= 54 #global variable

def func_1():
    print(a) #54
def func_2():
    a= 9 #local variable
    print(a) #9
def func_3():
    global a
    print(a) #54
    a= 9
    print(a) #9 

print(a) #54  
func_1() #54
func_2() #9
func_3() #54, 9
print(a) #54      