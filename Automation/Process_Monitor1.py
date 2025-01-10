import psutil

def ProcessDisplay():
    listprocess = []
    try:
        for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
            process_info = proc.info
            listprocess.append(process_info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    return listprocess

def main():
    print("Marvelous Infosystems: Python Automation & Machine Learning")
    print("Process Monitor")
    listprocess = ProcessDisplay()
    for elem in listprocess:
        print(elem)

if __name__ == "__main__":
    main()
