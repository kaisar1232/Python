#function accepts  parameters and call another function from it

def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Marvellous(Value1,Value2):
    Ans=Add(Value1,Value2)
    print("Addition Is ",Ans)
    
    Ans=Sub(Value1,Value2)
    print("Substraction Is ",Ans)
    
def main():
    Marvellous(11,7)

if __name__=="__main__":
    main()    