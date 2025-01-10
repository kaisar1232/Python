import MarvellousFMR

CheckEven = lambda No :  (No % 2 == 0)
Increse = lambda No:(No + 2)
Add = lambda A, B:(A + B)



def filterX(Task,Elements):
    Result = []
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result

def mapX(Task,Elements ):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result 

def reduceX(Task,Elements ):
    sum = 0
    
    for no in Elements:
        sum = sum + Task(sum,no)
        
    return sum 
   
def main():
    Data = []
    print("Enter number of elements")
    Size = int(input())
    
    print("Enter the elements")
    
    for i in range(Size):
        
        Value = int(input())
        Data.append(Value)
    print(Data)
    
    output = list(MarvellousFMR.filterX(CheckEven, Data))
    print("Output after filter",output)
    
    moutput = list(MarvellousFMR.mapX(Increse, output))
    print("output after mpm",moutput)
    
    poutput = MarvellousFMR.reduceX(Add, moutput)  
    print("output after reduse",poutput)

if __name__ == "__main__":
    main()
