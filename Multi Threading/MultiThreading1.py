import os
import threading

def Task1(value):
    print("PID Of Task 1:",os.getpid())
    print("Thread id  of Fisrst thread is",threading.current_thread())
    
def Task2(value):    
    print("PID Of Task 2:",os.getpid())
    
    print("Thread id  of Second thread is",threading.current_thread())

def main():
    print("PID Of Parent Proess :",os.getppid())
    
    print("Thread id  of main thread is",threading.current_thread())
    No = 5
    t1 = threading.Thread(target=Task1,args=(No,))
    t2 = threading.Thread(target=Task2,args=(No,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()  