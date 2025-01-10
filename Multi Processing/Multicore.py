# Get Count Of Cores Of Processors

import multiprocessing

def main():
    
    print("Number of Cores Are:",multiprocessing.cpu_count())
    
if __name__ == "__main__":
    main()
