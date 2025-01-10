import os
import sys
import psutil

def log_message(message, log_file):
    with open(log_file, 'a') as f:
        f.write(message + '\n')

def get_process_info(process_name):
    try:
        for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
            if process.info['name'] == process_name:
                return process.info
        return None
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        log_message(f"Error: {e}", 'error.log')
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: ProcInfo.py <process_name>")
        sys.exit(1)

    process_name = sys.argv[1]
    log_file = 'process_info.log'

    process_info = get_process_info(process_name)

    if process_info:
        log_message(f"Process Info: {process_info}", log_file)
        print(f"Process Info: {process_info}")
    else:
        log_message(f"Process {process_name} not found or an error occurred.", 'error.log')
        print(f"Process {process_name} not found or an error occurred.")

if __name__ == "__main__":
    main()
