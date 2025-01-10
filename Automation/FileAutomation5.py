import os
import sys
import time

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory:", DirName)
    flag = os.path.isabs(DirName)
    
    if flag == False:
        DirName=os.path.abspath(DirName)
    
    exist =os.path.isdir(DirName)
     
    if exist: 
        for foldername, subfoldername, filenames in os.walk(DirName):
            print("Current Directory Name:", foldername)
        
            for subname in subfoldername:
                print("Subfolder name is:", subname)

            for fname in filenames:
                #print(fname,":",os.path.getsize(fname))
                print(os.path.abspath(fname))
    else:
        print("Invalid Path")
        
def main():
    print("-------------- Automation Script --------------")
    
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        sys.exit(1)
    
    if sys.argv[1] == "-h" or sys.argv[1] == "-H":
        print("This automation script is used to perform File Automations")
        sys.exit(0)

    elif sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage : Name_Of_Script First_Argument")
        print("Example : Demo.py Marvellous")
        sys.exit(0)

    else:
        starttime = time.time()
        DirectoryTravel(sys.argv[1])
        endtime = time.time()

        print("The Script Took Time To Execute as", endtime - starttime)

if __name__ == "__main__":
    main()
