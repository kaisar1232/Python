import functools  

#we can use import functools for applying reduce funtion
#so we have to use <<<<<functools.reduce >>>>>> in our program

def main():
    Data = []
    print("Enter number of elements")
    Size = int(input())
    
    print("Enter the elements")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
        
    print(Data)
    output = list(filter((lambda No :  (No % 2 == 0)), Data))
    print("Output after filter",output)
    
    moutput = list(map((lambda No:(No + 2)), output))
    print("output after mpm",moutput)
    
    poutput = functools.reduce((lambda A, B:(A + B)), moutput)  
    print("output after reduse",poutput)

if __name__ == "__main__":
    main()
