from functools import reduce

def CheckEven(No):
    if No % 2 == 0:
        return True
    else:
        return False

def Increse(No):
    return No + 2

def Add(A, B):
    return A + B

def main():
    Data = [5, 4, 9, 8, 13, 17, 12, 18]
    print(Data)
    
    output = list(filter(CheckEven, Data))
    print(output)
    
    moutput = list(map(Increse, output))
    print(moutput)
    
    poutput = reduce(Add, moutput)  
    print(poutput)

if __name__ == "__main__":
    main()
