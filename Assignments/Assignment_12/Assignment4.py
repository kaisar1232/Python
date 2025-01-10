import os
import sys
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to get the process information
def get_process_info():
    process_info = []
    for process in psutil.process_iter(attrs=['name', 'pid', 'username']):
        process_info.append(f"Name: {process.info['name']}, PID: {process.info['pid']}, Username: {process.info['username']}")
    return process_info

# Function to create a log file in the specified directory
def create_log_file(directory, process_info):
    log_file_path = os.path.join(directory, 'process_log.txt')
    with open(log_file_path, 'w') as log_file:
        log_file.write("\n".join(process_info))
    return log_file_path

# Function to send the log file via email
def send_email(mail_id, log_file_path):
    from_email = 'your_email@gmail.com'  # Update with your email
    password = 'your_password'  # Update with your email password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = mail_id
    msg['Subject'] = 'Process Log'

    with open(log_file_path, 'r') as log_file:
        body = log_file.read()

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, mail_id, msg.as_string())
    server.quit()

def main():
    if len(sys.argv) != 3:
        print("Usage: ProcInfoLog.py <Directory> <Mail ID>")
        sys.exit(1)

    directory = sys.argv[1]
    mail_id = sys.argv[2]

    # Validate directory existence
    if not os.path.exists(directory):
        print("Error: The specified directory does not exist.")
        sys.exit(1)

    # Get process information
    process_info = get_process_info()

    # Create a log file in the specified directory
    log_file_path = create_log_file(directory, process_info)

    # Send the log file via email
    send_email(mail_id, log_file_path)

    print(f"Log file created at {log_file_path} and sent to {mail_id}.")

if __name__ == "__main__":
    main()
