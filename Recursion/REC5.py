#chenge recursion limit

import sys

def Display():
    print("Recursion limit is:",sys.getrecursionlimit())
A =sys.setrecursionlimit(1500)    
print("updeted limit is:",A)

def main():
    Display()
    
if __name__ == "__main__":
    main()    
    