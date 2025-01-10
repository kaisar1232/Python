import time
import multiprocessing

def fun(no):
    sum = 0
    
    for i in range(100000):
        sum = sum + (no * no)
    return sum
    
def main():
    
    
    print("Demonstation Of Serial Execution Using Single Core")
    
    starttime = time.time()
    p = multiprocessing.Pool()
    Result = []
    
    Result = p.map(fun,range(10000))
    p.close()
    p.join()
    
    endtime = time.time()
    
    print("Time Required To Execute The Application:",endtime-starttime)    
    
if __name__ == "__main__":
    main()    