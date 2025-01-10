#it can use open function for opening the existing file in directory

import os

def main():
    
    print("Enter the name of File that You Want to open for reading purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")  #it opens the file
        if fobj:
            print("File Succesfully Opened")
            fobj.close()   #use for closing the file
           
    else:    
        print("There is No Such File")
    
if __name__=="__main__":
    main()    