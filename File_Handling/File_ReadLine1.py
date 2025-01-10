#it prints the data from file 
#so we can give input file name as this file name so it will print the our typed code 

import os
def main():
    
    print("Enter the name of File that You Want to open for Reading purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")  #read mode used by 'r'
        if fobj:
            print("File Succesfully Opened in the read mode")
            
            print("Data From File Is ")
            for line in fobj:
                print(line)
                
            fobj.close()   
           
        else:    
            print("Unable To Open File")   
    
if __name__=="__main__":
    main()    