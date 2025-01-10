def main():
    try:
        num = int(input("Enter a number: "))
        
        if num < 0:
            print("Please enter a non-negative number.")
        else:
            print("*" * num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
