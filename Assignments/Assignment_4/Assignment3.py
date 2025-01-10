from functools import reduce

def filter_numbers(num):
    return num >= 70 and num <= 90

def add_ten(num):
    return num + 10

def multiply(x, y):
    return x * y

num_list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    num_list.append(num)

filtered_numbers = filter(filter_numbers, num_list)

mapped_numbers = map(add_ten, filtered_numbers)

result = reduce(multiply, mapped_numbers, 1)

print("Filtered and mapped numbers:", list(mapped_numbers))
print("Result of reduction:", result)
