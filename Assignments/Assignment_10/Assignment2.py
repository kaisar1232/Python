import os
import sys
import logging

# Configure logging to write to a log file
log_filename = "rename_log.txt"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

def rename_files(directory, old_extension, new_extension):
    try:
        # Validate directory exists
        if not os.path.exists(directory):
            raise Exception(f"Directory '{directory}' does not exist.")

        # Iterate through files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(old_extension):
                old_file_path = os.path.join(directory, filename)
                new_filename = filename[:-len(old_extension)] + new_extension
                new_file_path = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                logging.info(f"Renamed '{filename}' to '{new_filename}'")

        logging.info("Renaming completed.")
    except Exception as e:
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: DirectoryRename.py <directory> <old_extension> <new_extension>")
        sys.exit(1)

    directory = sys.argv[1]
    old_extension = sys.argv[2]
    new_extension = sys.argv[3]

    rename_files(directory, old_extension, new_extension)
