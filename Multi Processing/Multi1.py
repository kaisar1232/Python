import multiprocessing
import os

def Task1():
    
    print("Executing the first task1...")
    print("Pid Of Running process for Task1 ",os.getpid())
def Task2():
    print("Executing the second task...")
    print("Pid Of Running process Task2",os.getpid())
        
def main():
    print("Demonstation Of Multiprocessing")
    
    print("Pid Of Running process",os.getpid())
    print("PPid Of Running Parent process",os.getppid())
    
    
    Task1()
    Task2()
    
    
    
if __name__ == "__main__":
    main()    