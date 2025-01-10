### Module File can be imported in it ###

import Module

A =int(input("Enter the 1st Number"))
B =int(input("Enter the 2nd Number"))


result = 0

result=Module.Addition(A,B )
print("Addition is :",result)

result=Module.Substracton(A,B)
print("Substraction is :",result)

result=Module.Multiplication(A,B)
print("Multiplication is :",result)

result=Module.Division(A,B)
print("Division is :",result)

