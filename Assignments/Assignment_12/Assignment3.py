import os
import sys
import psutil
import datetime

def create_log_file(directory):
    log_file_path = os.path.join(directory, "process_info.log")
    try:
        with open(log_file_path, "w") as log_file:
            log_file.write("Process Name, PID, Username, Timestamp\n")
            for process in psutil.process_iter(attrs=['name', 'pid', 'username']):
                try:
                    process_info = process.info
                    log_file.write(f"{process_info['name']}, {process_info['pid']}, {process_info['username']}, {datetime.datetime.now()}\n")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ProcInfoLog.py <directory_name>")
        sys.exit(1)

    directory_name = sys.argv[1]

    if not os.path.exists(directory_name):
        print(f"Error: Directory '{directory_name}' does not exist.")
        sys.exit(1)

    create_log_file(directory_name)
    print(f"Process information logged to {directory_name}/process_info.log")
