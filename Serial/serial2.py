import time

def fun(no):
    sum = 0
    
    for i in range(100000):
        sum = sum + (no * no)
    return sum
    
def main():
    
    
    print("Demonstation Of Serial Execution Using Single Core")
    
    starttime = time.time()
    
    Result = []
    
    for no in range(10000):
        Result.append(fun(no))
    
    endtime = time.time()
    
    print("Time Required To Execute The Application:",endtime-starttime)    
    
if __name__ == "__main__":
    main()    