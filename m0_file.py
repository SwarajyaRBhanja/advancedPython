def greet(name):
    print(f"Good Morning, {name}")

# I want below lines to be executed only when it's called within same file, not on any other file which imports m0_file.py
print(__name__)
if __name__ == "__main__":
#__name__ evaluates to the name of the name of the module in python from where the program is ran
#If the module is directly being run from the command line the __name__ is set to string __main__
#thus the behaviour is used to check whether the module is run directly or imported to another file
    x = input("Please enter a name: \n")
    greet(x)
