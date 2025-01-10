import os
import sys
import hashlib
import shutil
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Function to calculate the checksum of a file
def calculate_checksum(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

# Function to find duplicate files in a directory
def find_duplicate_files(directory):
    file_checksums = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)

            if checksum in file_checksums:
                duplicates.append((file_path, file_checksums[checksum]))
            else:
                file_checksums[checksum] = file_path

    return duplicates

# Function to delete duplicate files and log their names
def delete_duplicates_and_log(duplicates, log_dir):
    log_file = os.path.join(log_dir, f"Duplicates_Log_{time.strftime('%Y%m%d_%H%M%S')}.txt")
    deleted_files = []

    with open(log_file, 'w') as log:
        for file_path, original_file_path in duplicates:
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
                log.write(f"Deleted: {file_path}\n")
            except Exception as e:
                log.write(f"Error deleting {file_path}: {str(e)}\n")

    return deleted_files

# Function to send an email with log file attachment
def send_email(receiver_email, log_file, stats):
    smtp_server = "your_smtp_server.com"  # Replace with your SMTP server
    sender_email = "your_sender_email@gmail.com"  # Replace with your sender email
    password = "your_email_password"  # Replace with your email password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Duplicate File Removal Report"

    body = f"Total number of files scanned: {stats['total_files_scanned']}\n"
    body += f"Starting time of scanning: {stats['start_time']}\n"
    body += f"Total number of duplicate files found: {stats['total_duplicates']}\n"

    message.attach(MIMEText(body, 'plain'))

    with open(log_file, 'rb') as log:
        attachment = MIMEApplication(log.read(), Name=os.path.basename(log_file))
        message.attach(attachment)

    try:
        server = smtplib.SMTP(smtp_server)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Main function to run the script
def main():
    if len(sys.argv) != 6:
        print("Usage: DuplicateFileRemoval.py <directory_path> <time_interval_minutes> <receiver_email>")
        sys.exit(1)

    directory = sys.argv[1]
    time_interval_minutes = int(sys.argv[2])
    receiver_email = sys.argv[3]

    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    log_dir = os.path.join(directory, "Marvellous")
    os.makedirs(log_dir, exist_ok=True)

    while True:
        try:
            start_time = time.strftime('%Y-%m-%d %H:%M:%S')
            duplicates = find_duplicate_files(directory)
            stats = {
                'total_files_scanned': len(os.listdir(directory)),
                'start_time': start_time,
                'total_duplicates': len(duplicates),
            }
            deleted_files = delete_duplicates_and_log(duplicates, log_dir)
            print(f"Deleted {len(deleted_files)} duplicate files.")
            send_email(receiver_email, deleted_files, stats)
            time.sleep(time_interval_minutes * 60)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
