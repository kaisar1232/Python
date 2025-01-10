#it uses 3 types of Exceptions

def main():
    try:
        print("Enter First Number")
        no1 = int(input())

        print("Enter Second Number")
        no2 = int(input())
        
        Ans = 0
       
        Ans = no1 / no2
        
    except ZeroDivisionError as zobj:
        print("Divide By Zero is not allowed",zobj)
        return
    except ValueError as zobj:
        print("invalid Input:",zobj)
        return
    
    except Exception as zobj:
        print("Exception Is Occured By:",zobj)
        return
    
    finally:
        print("Thank You For Using The Application")
        
    print("Division Is: ",Ans)
        
if __name__ == "__main__":
    main()