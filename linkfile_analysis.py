#!/usr/bin/env python3
import pylnk3

# Create a file for saving the output
with open("Linkfile_analysis.txt","w") as file1:

    # Retrieving relevant information by parsing link file.
    link_info = pylnk3.parse("./test.lnk")
    file1.write("Link File Information:\n %s" %link_info)
