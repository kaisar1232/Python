def Sub(A , B):
    if (A < B):
        A,B=B,A
        
    return A-B

def main():

   Ret = Sub(10,7)
   print("Substraction is:",Ret)
   
   Ret = Sub(7,10)
   print("Substraction is:",Ret)
   
if __name__=="__main__":
    main()