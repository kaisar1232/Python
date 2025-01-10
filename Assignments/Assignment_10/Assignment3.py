import os
import shutil
import sys
import logging

# Set up logging to write messages to a log file
logging.basicConfig(filename='automation.log', level=logging.INFO)

# Function to create a new directory if it doesn't exist
def create_directory(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)
            logging.info(f"Created directory: {directory_name}")
        else:
            logging.info(f"Directory already exists: {directory_name}")
    except Exception as e:
        logging.error(f"Error creating directory: {e}")
        sys.exit(1)

# Function to copy files from one directory to another
def copy_files(source_dir, destination_dir):
    try:
        create_directory(destination_dir)
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
                logging.info(f"File copied: {filename}")
    except Exception as e:
        logging.error(f"Error copying files: {e}")
        sys.exit(1)

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: DirectoryCopy.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    try:
        if not os.path.exists(source_directory):
            logging.error("Source directory does not exist.")
            sys.exit(1)

        copy_files(source_directory, destination_directory)
        logging.info("Files copied successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)
