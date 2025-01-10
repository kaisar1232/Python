def main():
    n = int(input("Enter the number of elements: "))
    num_list = []
    
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        num_list.append(num)
    
    target_num = int(input("Enter the number to find frequency for: "))
    
    frequency = num_list.count(target_num)
    
    print(f"The frequency of {target_num} in the list is {frequency}")

if __name__ == "__main__":
    main()
