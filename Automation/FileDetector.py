import os
import hashlib
import sys

def hashfile(path, blocksize=1024):
    try:
        fd = open(path, 'rb')
        hasher = hashlib.md5()
        buf = fd.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = fd.read(blocksize)
        fd.close()
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error hashing file {path}: {str(e)}")

def FindDuplicate(path):
    flag = os.path.isabs(path)
    if not flag:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                filepath = os.path.join(dirName, filen)
                file_hash = hashfile(filepath)
                if file_hash in dups:
                    dups[file_hash].append(filepath)
                else:
                    dups[file_hash] = [filepath]
    else:
        print("Invalid Path")
    return dups

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print("Duplicates Found:")
        print("The following files are identical:")
        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print(subresult)
    else:
        print("No duplicate files found.")

def main():
    print("Marvellous Infosystems by Piyush Khaimar -")
    print("Application name: " + sys.argv[0])
    
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        exit()

    if sys.argv[1] in {"-h", "--help"}:
        print("This Script is used to traverse a specific directory and display duplicate files.")
        print("Usage: python script.py /path/to/directory")
        exit()
    
    try:
        arr = FindDuplicate(sys.argv[1])
        PrintDuplicate(arr)
    except ValueError:
        print("Error: Invalid datatype of input")

if __name__ == "__main__":
    main()
