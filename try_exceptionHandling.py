while(True):
    print("Press q to quit")
    a= input("Please enter a number: ")
    if a=='q':
        break
    try:
        a= int(a)
        if a>6:
            print("You have entered a number greater than 6.")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")  #  Your input resulted in an error invalid literal for int() with base 10: 'w'  
print("Thanks for playing this game.")          