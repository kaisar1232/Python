def Addition(No1, No2):
    question= 0
    question= No1 + No2
    return question

def main():
    Value1= int(input("enter 1st No:"))
    Value2= int(input("enter 2st No:"))

    Answer=0
    Answer= Addition(Value1, Value2)

    print("Addition is",Answer)

if __name__ =="__main__":    #it was starter
    main()