import os
def main():
    
    print("Enter the name of File that You Want to open for Reading purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")  #read mode used by 'r'
        if fobj:
            print("File Succesfully Opened in the read mode")
            
            line1 = fobj.readline()
            line2 = fobj.readline()
            line3 = fobj.readline()
            
            print("First Line iS:",line1)
            print("Second Line iS:",line2)
            print("Third Line iS:",line3)
            
            fobj.close()   
           
        else:    
            print("Unable To Open File")   
    
if __name__=="__main__":
    main()    