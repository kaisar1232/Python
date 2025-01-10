import os
def main():
    
    print("Enter the name of File that You Want to open for Reading purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")  #read mode used by 'r'
        if fobj:
            print("File Succesfully Opened in the read mode")
            
            Data = fobj.read(10)
            print("Data From File is:",Data)
            
            fobj.close()   
           
        else:    
            print("Unable To Open File")   
    
if __name__=="__main__":
    main()    