def get_factors_sum(number):
    factors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factors_sum += i
    return factors_sum

def main():
    
    
    number = int(input("Enter a number: "))
    if number < 0:
        print("Please enter a positive integer.")
    else:
        result = get_factors_sum(number)
        print(f"The sum of factors of {number} is: {result}")
    

if __name__ == "__main__":
    main()
