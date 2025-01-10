import threading

def calculate_factors(number, is_even, result_lock, result_list):
    factors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            if is_even and i % 2 == 0:
                factors_sum += i
            elif not is_even and i % 2 != 0:
                factors_sum += i

    with result_lock:
        result_list.append(factors_sum)

def main():
    num = int(input("Enter an integer: "))
    result_lock = threading.Lock()
    result_list = []

    evenfactor_thread = threading.Thread(target=calculate_factors, args=(num, True, result_lock, result_list))
    oddfactor_thread = threading.Thread(target=calculate_factors, args=(num, False, result_lock, result_list))

    evenfactor_thread.start()
    oddfactor_thread.start()

    evenfactor_thread.join()
    oddfactor_thread.join()

    even_sum = result_list[0]
    odd_sum = result_list[1]

    print(f"Sum of even factors: {even_sum}")
    print(f"Sum of odd factors: {odd_sum}")
    print("exit from main")

if __name__ == "__main__":
    main()
