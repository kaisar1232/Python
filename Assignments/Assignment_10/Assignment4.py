import os
import shutil
import sys

# Function to copy files with a specific extension from one directory to another
def copy_files_with_extension(source_dir, destination_dir, file_extension):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            print(f"Created destination directory '{destination_dir}'")

        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)

            # Check if the file has the desired extension
            if filename.endswith(file_extension):
                destination_file = os.path.join(destination_dir, filename)
                shutil.copy2(source_file, destination_file)
                print(f"Copying '{filename}' to '{destination_dir}'")

        print("File copy completed successfully.")
    except FileNotFoundError as e:
        log_error(e)
    except Exception as e:
        log_error(e)

# Function to log error messages to a log file
def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(str(error_message) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: DirectoryCopyExt.py <source_directory> <destination_directory> <file_extension>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    file_extension = sys.argv[3]

    copy_files_with_extension(source_directory, destination_directory, file_extension)
