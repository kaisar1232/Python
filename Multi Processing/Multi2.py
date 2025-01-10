import multiprocessing
import os
 

def Task1(Value):
    
    print("Executing the first task1...")
    print("Pid Of Running process for Task1 ",os.getpid())
    
def Task2(Value):
    print("Executing the second task...")
    print("Pid Of Running process Task2",os.getpid())
        
def main():
    print("Demonstation Of Multiprocessing")
    
    print("Pid Of Running process",os.getpid())
    print("PPid Of Running Parent process",os.getppid())
    
    
    No = 5
    
    p1 = multiprocessing.Process(target=Task1,args=(No,))
    p2 = multiprocessing.Process(target=Task2,args=(No,))
   
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
if __name__ == "__main__":
    main()    