import threading

def evenlist_thread(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    print("Even List Sum:", even_sum)

def oddlist_thread(numbers):
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    print("Odd List Sum:", odd_sum)

def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_thread = threading.Thread(target=evenlist_thread, args=(input_list,))
    odd_thread = threading.Thread(target=oddlist_thread, args=(input_list,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()
