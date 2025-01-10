#User input Values to command Line Argumets
#Addition of two numbers

import sys

def main():

    print("No.of Command Line Arguments:",sys.argv)
    
    val1=int(sys.argv[1])
    val2=int(sys.argv[2])
    Ans=val1 + val2
    
    print("addition is:",Ans)
       
if __name__ == "__main__":
    main()   
