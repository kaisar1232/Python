#   in this program we can create our own functions
CheckEven = lambda No :  (No % 2 == 0)
Increse = lambda No:(No + 2)
Add = lambda A, B:(A + B)

#Task:Name Of Function
#Elements:List Of Data Elements

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
    
    output = list(filterX(CheckEven, Data))
    print("Output after filter",output)
    
    moutput = list(mapX(Increse, output))
    print("output after mpm",moutput)
    
    poutput = reduceX(Add, moutput)  
    print("output after reduse",poutput)

if __name__ == "__main__":
    main()
