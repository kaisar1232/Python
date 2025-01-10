def find_maximum(numbers):
    if not numbers:
        return None  
    
    max_number = numbers[0]  
    
    for num in numbers:
        if num > max_number:
            max_number = num
    
    return max_number

def main():
    n = int(input("Enter the number of elements: "))
    num_list = []
    
    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        num_list.append(num)
    
    maximum = find_maximum(num_list)
    
    if maximum is not None:
        print(f"The maximum number is: {maximum}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()
