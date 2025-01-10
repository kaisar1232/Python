def fun(no):
    sum = 0
    
    for i in range(100000):
        sum = sum + (no * no)
    return sum
    
def main():
    
    
    print("Demonstation Of Serial Execution Using Single Core")
    
    ret =fun(10)
    
    print(ret)
    
if __name__ == "__main__":
    main()    