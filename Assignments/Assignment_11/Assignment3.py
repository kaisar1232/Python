import os
import hashlib
import argparse

def get_file_hash(file_path):
    """Calculate and return the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # 64 KB buffer
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """Find duplicate files in the given directory."""
    file_hash_map = {}
    duplicate_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = get_file_hash(file_path)

            if file_hash in file_hash_map:
                duplicate_files.append(file_path)
            else:
                file_hash_map[file_hash] = file_path

    return duplicate_files

def delete_duplicate_files(duplicate_files):
    """Delete duplicate files."""
    for file_path in duplicate_files:
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def log_to_file(duplicate_files, log_file):
    """Log duplicate file names to a log file."""
    with open(log_file, 'w') as log:
        for file_path in duplicate_files:
            log.write(file_path + '\n')

def main():
    parser = argparse.ArgumentParser(description="Delete duplicate files in a directory")
    parser.add_argument("directory", help="Directory name to search for duplicate files")
    args = parser.parse_args()

    directory = args.directory
    log_file = "Log.txt"

    if not os.path.exists(directory):
        print("Directory not found.")
        return

    duplicate_files = find_duplicate_files(directory)

    if not duplicate_files:
        print("No duplicate files found.")
        return

    log_to_file(duplicate_files, log_file)
    delete_duplicate_files(duplicate_files)
    print(f"Deleted {len(duplicate_files)} duplicate files. Duplicate file names are logged in {log_file}.")

if __name__ == "__main__":
    main()
