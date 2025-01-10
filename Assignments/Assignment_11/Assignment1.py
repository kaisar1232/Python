import os
import hashlib
import argparse
import logging

# Function to calculate checksum (SHA-256) of a file
def calculate_checksum(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

# Function to get a list of all files in a directory
def get_files_in_directory(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# Function to display checksum of all files in a directory
def display_checksums(directory):
    file_list = get_files_in_directory(directory)
    
    # Create a log file
    log_file = f"{directory}_checksums.log"
    logging.basicConfig(filename=log_file, level=logging.INFO)
    
    for file_path in file_list:
        try:
            checksum = calculate_checksum(file_path)
            logging.info(f"File: {file_path}, Checksum: {checksum}")
        except Exception as e:
            logging.error(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate checksum of files in a directory.")
    parser.add_argument("directory", help="Directory name to calculate checksums for.")
    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print(f"Directory '{args.directory}' does not exist.")
    else:
        display_checksums(args.directory)
        print(f"Checksums calculated and logged in '{args.directory}_checksums.log'")
