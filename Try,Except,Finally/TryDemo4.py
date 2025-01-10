#it can avoid any of exceptional error by using "Exception"
def main():
    
    print("Enter First Number")
    no1 = int(input())
    
    print("Enter Second Number")
    no2 = int(input())
            
    Ans = 0
    try:   
        Ans = no1 / no2
        
    except Exception as zobj:
        print("Exception is occured as:",zobj)
        return
        
    print("Division Is: ",Ans)
        
if __name__ == "__main__":
    main()