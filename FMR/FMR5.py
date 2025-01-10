from functools import reduce

CheckEven = lambda No :  (No % 2 == 0)
     
Increse = lambda No:(No + 2)

Add = lambda A, B:(A + B)

def main():
    Data = []
    print("Enter number of elements")
    Size = int(input())
    
    print("Enter the elements")
    
    for i in range(Size):
        
        Value = int(input())
        Data.append(Value)
        
    print(Data)
    
    output = list(filter(CheckEven, Data))
    print("Output after filter",output)
    
    moutput = list(map(Increse, output))
    print("output after mpm",moutput)
    
    poutput = reduce(Add, moutput)  
    print("output after reduse",poutput)

if __name__ == "__main__":
    main()
