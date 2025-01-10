class Arithmatic:
    
    def __init__(self,A,B):
        
        print("inside Constructor")
        self.No1 = A
        self.No2 = B
        
    
    def Addition(self):
        Ans = 0
        Ans = self.No1+self.No2
        return Ans
        
    def Substraction(self):
        Ans = 0
        Ans = self.No1-self.No2 
        return Ans   

def main():
   Value1 = int(input("enter 1st naum")) 
   Value2 = int(input("enter 2nd naum")) 
   
   obj1 = Arithmatic(Value1,Value2)
   Ret = obj1.Addition()
   print("Addition is ",Ret)
   
   Ret = obj1.Substraction()
   print("Substraction is ",Ret)
   
   Value1 = int(input("enter 1st naum")) 
   Value2 = int(input("enter 2nd naum")) 
   
   obj2 = Arithmatic(Value1,Value2)
   Ret = obj2.Addition()
   print("Addition is ",Ret)
   
   Ret = obj2.Substraction()
   print("Substraction is ",Ret)

 
if __name__ == "__main__":
    main()   