import os
import sys
import logging

# Set up logging to write messages to a log file
logging.basicConfig(filename='automation_script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def find_files_with_extension(directory, extension):
    try:
        # Validate if the directory exists
        if not os.path.exists(directory):
            logging.error(f"The directory '{directory}' does not exist.")
            return
        
        # Validate if the given path is a directory
        if not os.path.isdir(directory):
            logging.error(f"'{directory}' is not a directory.")
            return

        # List all files in the directory with the specified extension
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    logging.info(f"Found file: {os.path.join(root, file)}")
                    print(os.path.join(root, file))  # You can also choose to print to console

    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python DirectoryFileSearch.py <directory_name> <file_extension>")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]

    find_files_with_extension(directory, extension)

if __name__ == "__main__":
    main()
