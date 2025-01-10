def Addition(No1,No2):
    Ans =0
    Ans = No1 + No2
    return Ans

def Substraction(No1,No2):
    Ans =0
    Ans = No1 - No2
    return Ans

def main():
   Value1 = int(input("enter 1st naum")) 
   Value2 = int(input("enter 2nd naum")) 
 
   Ret = Addition(Value1,Value2)
   print(Ret)

   Ret = Substraction (Value1,Value2)
   print(Ret) 
if __name__ == "__main__":
    main()   