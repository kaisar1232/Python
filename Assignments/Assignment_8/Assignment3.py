#when i input 5 it prints 5 4 3 2 1
def print_pattern(n):
    if n > 0:
        print(n, end=' ')
        print_pattern(n - 1)

    num = int(input("Enter a number: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        print("Pattern:")
        print_pattern(num)
