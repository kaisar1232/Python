def find_minimum(numbers):
    if not numbers:
        return None  
    
    min_num = numbers[0]  
    
    for num in numbers:
        if num < min_num:
            min_num = num
    
    return min_num

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    minimum = find_minimum(numbers)
    
    if minimum is not None:
        print(f"The minimum number is: {minimum}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()
