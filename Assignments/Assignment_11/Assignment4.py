import os
import sys
import hashlib
import time

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

# Function to find and delete duplicate files in a directory
def delete_duplicate_files(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    duplicate_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash in duplicate_files:
                duplicate_files[file_hash].append(file_path)
            else:
                duplicate_files[file_hash] = [file_path]

    # Delete duplicate files and write their names to the log file
    with open("Log.txt", "w") as log_file:
        for _, duplicates in duplicate_files.items():
            if len(duplicates) > 1:
                log_file.write("Duplicate Files:\n")
                for duplicate in duplicates:
                    log_file.write(f"{duplicate}\n")
                    os.remove(duplicate)

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicateRemoval.py <directory_name>")
        sys.exit(1)

    directory_name = sys.argv[1]
    start_time = time.time()

    try:
        delete_duplicate_files(directory_name)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.2f} seconds")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
