#it can use "Append" function for opening the existing file in directory

import os
def main():
    
    print("Enter the name of File that You Want to open for Writing purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"a")  #append mode used by 'a'
        if fobj:
            print("File Succesfully Opened in the append mode")
            print("Enter the data that you want to write in file")
            Data=input()
            
            fobj.write(Data)  #Write The Data Into  the File
            
            fobj.close()   
           
        else:    
            print("Unable To Open File")   
    
if __name__=="__main__":
    main()    