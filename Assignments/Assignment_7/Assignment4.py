import threading

def count_small_characters(s):
    count = sum(1 for char in s if char.islower())
    print(f"Thread ID: {threading.get_ident()} - Name: {threading.current_thread().name}")
    print(f"Number of small characters: {count}")

def count_capital_characters(s):
    count = sum(1 for char in s if char.isupper())
    print(f"Thread ID: {threading.get_ident()} - Name: {threading.current_thread().name}")
    print(f"Number of capital characters: {count}")

def count_digits(s):
    count = sum(1 for char in s if char.isdigit())
    print(f"Thread ID: {threading.get_ident()} - Name: {threading.current_thread().name}")
    print(f"Number of digits: {count}")

def main():
    input_string = input("Enter a string: ")

    small_thread = threading.Thread(target=count_small_characters, args=(input_string,))
    capital_thread = threading.Thread(target=count_capital_characters, args=(input_string,))
    digits_thread = threading.Thread(target=count_digits, args=(input_string,))

    small_thread.name = "Small Characters Thread"
    capital_thread.name = "Capital Characters Thread"
    digits_thread.name = "Digits Thread"

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

if __name__ == "__main__":
    main()
