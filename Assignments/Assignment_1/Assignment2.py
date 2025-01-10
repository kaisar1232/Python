def Chknum(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# Test the function
try:
    num = int(input("Enter a number: "))
    Chknum(num)
except ValueError:
    print("Invalid input. Please enter a valid number.")
