##### Command Line Arguments ####
#python command1.py Marvellous 11  


import sys

def main():
    
    print("No.of Command Line Arguments:",sys.argv)
    
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    
    
if __name__ == "__main__":
    main()   
