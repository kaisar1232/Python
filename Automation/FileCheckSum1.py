'''Automation Script which accepts directory name from user and display all names & checksum of file from that directory'''

import os
import hashlib
import sys

def hashfile(path, blocksize=1024):
    # Open the file in binary read mode
    afile = open(path, 'rb')
    hasher = hashlib.md5()  # Create an MD5 hash object

    while True:
        buf = afile.read(blocksize)  # Read a block of data
        if not buf:
            break
        hasher.update(buf)  # Update the hash object with the data from the block

    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    # Check if the path is absolute, and if not, make it absolute
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    # Check if the path is a directory
    if os.path.isdir(path):
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is: " + dirName)
            for filename in fileList:
                filepath = os.path.join(dirName, filename)  # Get the full path of the file
                file_hash = hashfile(filepath)  # Calculate the MD5 checksum
                print(f"File: {filename}, MD5 Checksum: {file_hash}")
    else:
        print("Error: The provided path is not a directory.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py AbsolutePath_of_Directory")
        sys.exit(1)

    directory_path = sys.argv[1]
    try:
        DisplayChecksum(directory_path)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
