class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter Value1: "))
        self.Value2 = float(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Cannot divide by zero."

obj1 = Arithmetic()
obj1.Accept()
print("Addition:", obj1.Addition())
print("Subtraction:", obj1.Subtraction())
print("Multiplication:", obj1.Multiplication())
print("Division:", obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition:", obj2.Addition())
print("Subtraction:", obj2.Subtraction())
print("Multiplication:", obj2.Multiplication())
print("Division:", obj2.Division())
class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter Value1: "))
        self.Value2 = float(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Cannot divide by zero."

obj1 = Arithmetic()
obj1.Accept()
print("Addition:", obj1.Addition())
print("Subtraction:", obj1.Subtraction())
print("Multiplication:", obj1.Multiplication())
print("Division:", obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition:", obj2.Addition())
print("Subtraction:", obj2.Subtraction())
print("Multiplication:", obj2.Multiplication())
print("Division:", obj2.Division())
