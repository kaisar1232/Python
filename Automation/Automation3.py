from sys import argv  # Import argv from the sys module
from Arithmatic import Addition  # Import the Addition function from the Arithmetic module

def main():
    print("---------Automation Script---------")
    print("Automation Script Name:", argv[0])
    
    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":  # Use '==' for comparison
            print("This Automation Script is used to perform addition of two numbers")
            exit()
        
        elif argv[1] == "-u" or argv[1] == "-U":  # Use '==' for comparison
            print("Usage: Name_of_Script First_Argument Second_Argument")
            print("Example: Demo.py 11 10")
            exit()
        else:
            print("There is No Such Option To Handle")

    if len(argv) != 3:
        print("Invalid Number of Arguments")
        exit()
    else:
        Ret = Addition(int(argv[1]), int(argv[2]))  # Separate the int() calls
        print("Addition Is:", Ret)

if __name__ == "__main__":
    main()
