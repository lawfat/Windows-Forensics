#!/usr/bin/env python3

# Reference: https://mattcasmith.net/2018/11/23/python-forensics-tools-windows-prefetch/

import os, time

def main():

    prefetch_directory = "/home/kajol/LawFact/PrefetchAnalysis/prefetch_samples/"

    # Get the list of files from prefetch directory
    prefetch_files = os.listdir(prefetch_directory)
    
    # Create file for saving the output
    with open("PrefetchAnalysis.txt", "w") as file1:

        # Iterate over each file to get full path. 
        for pf_file in prefetch_files:

            full_path = prefetch_directory + pf_file
        
            # Trimming the directory hash from end of the Prefetch filename to get executable name
            exe_name = pf_file[:-12]

            file1.write("Executable filename: %s\n" %exe_name)

            # Retrieving timestamp of file created and convert it into readable format
            created = os.path.getctime(full_path)
            created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created))

            accessed = os.path.getatime(full_path)
            accessed = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(accessed))

            # Retrieving timestamp of file modified and convert it into readable format
            file_modified = os.path.getmtime(full_path)
            file_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_modified))
        
            file1.write("File modified time: %s\n" %file_modified)
            file1.write("file accessed time: %s\n" %accessed)
            file1.write("file creation time: %s\n" %created)
            file1.write("\n")

if __name__ == "__main__":
    main()

