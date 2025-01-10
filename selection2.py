def CheckEven(Value):
    Result =Value % 2

    if(Result==0):
        
        print("mum is even")
    else:
        print("num is odd")     
def main():
    No=0
    print("enter num:")
   
    no=int(input())

    CheckEven(No)

if __name__ == "__main__":
    main()    