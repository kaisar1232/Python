#in this case we can check exist file is there or not
#if alredy exist then it prints line No.12

import os.path

def main():
    
    print("Enter the name of File that You Want to Create : ")
    File_name = input()
    
    if os.path.exists(File_name):
        print("Unable To Create File Becuse It Already Existing")
    else:    
        fobj = open(File_name,"x")
    
if __name__=="__main__":
    main()    