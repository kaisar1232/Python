import psutil

def ProcessDisplay():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo_str = f"Process ID: {pinfo['pid']}, Name: {pinfo['name']}, Username: {pinfo['username']}, Memory Usage (MB): {proc.memory_info().vms / (1024 * 1024)}"
            listprocess.append(pinfo_str)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Marvelous Infosystems: Python Automation & Machine Learning")
    print("Process Monitor with memory usage")
    listprocess = ProcessDisplay()
    for elem in listprocess:
        print(elem)

if __name__ == "__main__":
    main()
