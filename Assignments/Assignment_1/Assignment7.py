def is_divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False


user_input = int(input("Enter a number: "))

result = is_divisible_by_5(user_input)
print(f"{user_input} is divisible by 5: {result}")
