import Module

def main():
    value1=int(input("enter 1st Number:"))
    value2=int(input("enter 3nd Number:"))
    
    result=0
    result=Module.Addition(value1 ,value2)
    print("Addition is",result)
    
    result=Module.Substracton(value1 ,value2)
    print("Substracton is",result)
    
    result=Module.Multiplication(value1 ,value2)
    print("Multiplication is",result)
    
if __name__ == "__main__":
    main()
    
    
    
    
   