from functools import reduce

def is_even(n):
    return n % 2 == 0

def square(n):
    return n ** 2

def add(x, y):
    return x + y

num_list = []
num_count = int(input("Enter the number of elements in the list: "))
for _ in range(num_count):
    num = int(input("Enter a number: "))
    num_list.append(num)

even_numbers = list(filter(is_even, num_list))

squared_numbers = list(map(square, even_numbers))

sum_of_squares = reduce(add, squared_numbers)

print("Original list:", num_list)
print("Even numbers:", even_numbers)
print("Squares of even numbers:", squared_numbers)
print("Sum of squares:", sum_of_squares)
