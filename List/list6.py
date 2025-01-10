
def main():
    print("Enter no.of elemnts that you eant to store")
    Length = int(input())
    
    
    Arr = list()
    
    print("enter the elemets")
    
    for i in range(Length):
        Value=int(input())
        Arr.append(Value)
        
    print("elements from list are:")
    
    for i in range(Length):
        print(Arr[i])    
    
if __name__ == "__main__":
    main()   
         
