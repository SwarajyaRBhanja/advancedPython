
#lambda: functions created using an expression using lambda keyword
#syntax: lambda arguments: expressions

x= int(input("Please enter a number"))
y=lambda l:l+5
cal= lambda m,n,p: m+n-p
print(y(x))
print(cal(8,5,2))