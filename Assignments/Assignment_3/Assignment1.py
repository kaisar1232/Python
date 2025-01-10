def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    total = sum(numbers)
    print(f"The sum of all elements is: {total}")

if __name__ == "__main__":
    main()
