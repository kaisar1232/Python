import os
def main():
    
    print("Enter the name of File")
    File_name = input()
    
    if os.path.exists(File_name):  
        print("File Is There") 
           
    else:    
        print("Unable To Open File")   
    
if __name__=="__main__":
    main()    