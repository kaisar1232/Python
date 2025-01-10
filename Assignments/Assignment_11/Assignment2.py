import os
import sys

def create_log_file(log_filename):
    try:
        log_file = open(log_filename, 'w')
        return log_file
    except Exception as e:
        raise Exception(f"Error creating log file: {str(e)}")

def list_duplicates(seq):
    tally = {}
    for i in seq:
        if i in tally:
            tally[i] += 1
        else:
            tally[i] = 1
    return [(key, val) for key, val in tally.items() if val > 1]

def find_duplicate_files(directory):
    try:
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append((file, file_path))

        duplicates = list_duplicates(file_list)
        return duplicates
    except Exception as e:
        raise Exception(f"Error finding duplicate files: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicate.py <directory_name>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("Error: Directory does not exist.")
        sys.exit(1)
    
    log_filename = 'Log.txt'
    log_file = create_log_file(log_filename)

    try:
        duplicates = find_duplicate_files(directory)
        if not duplicates:
            log_file.write("No duplicate files found.")
        else:
            log_file.write("Duplicate files:\n")
            for duplicate in duplicates:
                log_file.write(f"{duplicate[0]} - {duplicate[1]}\n")
        print(f"Duplicate files information written to {log_filename}")
    except Exception as e:
        log_file.write(f"Error: {str(e)}")
    finally:
        log_file.close()

if __name__ == "__main__":
    main()
