#when i input 5 it prints * * * * *

def print_asterisks(n):
   
    if n == 0:
        return
    print('*', end=' ')
    print_asterisks(n - 1)

n = int(input("Enter a number: "))
print_asterisks(n)
