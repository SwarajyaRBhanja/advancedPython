
#write a program to open 3 files 1.txt, 2.txt & 3.txt.
#If any of these files are not present, a message without exiting the program must be printed prompting the same.

def readFile(filename):

    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename[-5:]} is not found")        
readFile("/Users/swarajyabhanja/Desktop/Python/advancedPython/1.txt")
readFile("/Users/swarajyabhanja/Desktop/Python/advancedPython/2.txt")
readFile("/Users/swarajyabhanja/Desktop/Python/advancedPython/3.txt")
readFile("/Users/swarajyabhanja/Desktop/Python/advancedPython/4.txt")

