from functools import reduce

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num_list = []
n = int(input("Enter the number of elements in the list: "))
for _ in range(n):
    num = int(input("Enter a number: "))
    num_list.append(num)

filtered_nums = list(filter(is_prime, num_list))

mapped_nums = list(map(lambda x: x * 2, filtered_nums))

max_num = reduce(lambda x, y: x if x > y else y, mapped_nums)

print("Original List:", num_list)
print("Filtered Prime Numbers:", filtered_nums)
print("Mapped Doubled Numbers:", mapped_nums)
print("Maximum Number:", max_num)
