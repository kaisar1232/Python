class Demo:
   def __init__(self,Value1,Value2):  #Constructor
      
      print("inside init method")
      self.No1=Value1
      self.No2=Value2
      
   def Display(self): #instance method
      
      print("Value Of No1:",self.No1)
      print("Value Of No2:",self.No2)
         
def main():
   
   print("Obeject Orientation Concept")
   obj1 = Demo(10,20) #__init__(10,20)
   obj2 = Demo(11,21) #__init__(11,21)
   
   obj1.Display()
   obj2.Display()
     
     
if __name__ == "__main__":
   main()   