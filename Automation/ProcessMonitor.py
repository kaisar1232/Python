#It Displays The Totoal Running Processes On Our Processor`s Ram

import psutil        #Used To Handle Process Subsystem

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            
            listprocess.append(pinfo);
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor")
    
    listprocess = ProcessDisplay()
    
    icnt = 0
    for elem in listprocess:
        icnt+=1
        print(elem)
        
    print("Number Of Running Processes Are:",icnt)
    
if __name__=="__main__":
    main()






