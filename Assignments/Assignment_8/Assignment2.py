#when i input 5 it prints 1 2 3 4 5
def display_pattern(n):
    if n > 0:
        display_pattern(n - 1)
        print(n, end=' ')

num = int(input("Enter a number: "))

display_pattern(num)
