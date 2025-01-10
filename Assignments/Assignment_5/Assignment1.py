class Demo:
    Value = "Class Variable"
    
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
    
    def Fun(self):
        print("Inside Fun method:")
        print("no1:", self.no1)
        print("no2:", self.no2)
        print("Value:", self.Value)
    
    def Gun(self):
        print("Inside Gun method:")
        print("no1:", self.no1)
        print("no2:", self.no2)
        print("Value:", self.Value)
        
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
