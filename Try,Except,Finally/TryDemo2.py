#exeption Handling
def main():
    
    print("Enter First Number")
    no1 = int(input())
    
    print("Enter Second Number")
    no2 = int(input())
            
    Ans = 0
    try:   
        Ans = no1 / no2
        
    except ZeroDivisionError as zobj:
        print("Divide By Zero is not allowed",zobj)
                
    print("Division Is: ",Ans)
        
if __name__ == "__main__":
    main()