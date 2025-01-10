#it prints the data from file 
#so we can give input file name as this file name so it will print the our typed code 

import os
def main():
    
    print("Enter the name of File:")
    File = input()
    
    if os.path.exists(File):
        obj = open(File,"r")  #read mode used by 'r'
        if obj:            
            print("Data From File Is ")
            for line in obj:
                print(line)
        obj.close()       
if __name__=="__main__":
    main()    