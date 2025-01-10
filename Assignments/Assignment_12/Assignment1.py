import sys
import psutil
import logging
from datetime import datetime

# Create a logger and configure it to log messages to a file
logging.basicConfig(filename='proc_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_message(message):
    # Log the message with a timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'{timestamp} - {message}'
    logging.info(log_entry)

def get_process_info():
    try:
        log_message("Getting process information...")
        for process in psutil.process_iter(attrs=['name', 'pid', 'username']):
            log_message(f"Name: {process.info['name']} | PID: {process.info['pid']} | Username: {process.info['username']}")
        log_message("Process information retrieved successfully.")
    except Exception as e:
        log_message(f"Error: {str(e)}")

if __name__ == "__main__":
    log_message("Starting ProcInfo.py")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--file":
        # Log to console
        print("Logging to console. To log to a file, run the script without the '--file' flag.")
        get_process_info()
    else:
        get_process_info()

    log_message("Exiting ProcInfo.py")
