class Numbers:
    def __init__(self, value):
        self.Value = value
    
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        return self.Value == self.SumFactors()
    
    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors
    
    def SumFactors(self):
        return sum(self.Factors())

num1 = Numbers(6)
print(f"Factors of num1: {num1.Factors()}")
print(f"Sum of factors of num1: {num1.SumFactors()}")
print(f"Is num1 prime? {num1.ChkPrime()}")
print(f"Is num1 perfect? {num1.ChkPerfect()}")

num2 = Numbers(28)
print(f"Factors of num2: {num2.Factors()}")
print(f"Sum of factors of num2: {num2.SumFactors()}")
print(f"Is num2 prime? {num2.ChkPrime()}")
print(f"Is num2 perfect? {num2.ChkPerfect()}")
