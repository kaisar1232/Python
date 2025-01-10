import os

def main():
    
    print("Enter the name of File that You Want to Delete : ")
    File_name = input()
    
    if os.path.exists(File_name):
        os.remove(File_name)
    else:    
        print("There is No Such File")
    
if __name__=="__main__":
    main()   