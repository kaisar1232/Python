import threading

def print_numbers_forward():
    for i in range(1, 51):
        print(f"Thread 1: {i}")
        
def print_numbers_reverse():
    for i in range(50, 0, -1):
        print(f"Thread 2: {i}")

# Create thread objects
thread1 = threading.Thread(target=print_numbers_forward)
thread2 = threading.Thread(target=print_numbers_reverse)

# Start thread1
thread1.start()

# Wait for thread1 to complete
thread1.join()

# Start thread2 after thread1 is completed
thread2.start()

# Wait for thread2 to complete
thread2.join()

print("Both threads have completed.")
