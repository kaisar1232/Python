from sys import *

def main():

    print("---------Automation Script---------")
    
    print("Automation Script Name:",argv[0])
    
    if(len(argv)==2):
        if(argv[1]=="-h"or argv[1]=="-H"):   #Flag for displaying help
        
            print("this Automation Script is used to perform addition of two numbers")
            exit()
        
        elif(argv[1]=="-u"or argv[1]=="-U"):    #Flag for displaying usage of script
        
            print("Usage:Name_of_Script First_Argument Secpnd_Argument") 
            print("Example:Demo.py 11 10") 
            exit()  
        else:
            print("there Is No Such Option To Handle")
        
    if(len(argv)!=3):
        print("Invalid Number of Aruments")
        exit()    
if __name__ == "__main__":
    main()   