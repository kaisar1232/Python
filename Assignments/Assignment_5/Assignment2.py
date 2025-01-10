class Circle:
    PI = 3.14
    
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
        
    def Accept(self):
        self.radius = float(input("Enter the radius of the circle: "))
        
    def CalculateArea(self):
        self.area = Circle.PI * (self.radius ** 2)
        
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius
        
    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Circumference: {self.circumference}")


circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

circle2 = Circle()
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()
