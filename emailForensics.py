#!/usr/bin/env python3

# Reference: https://github.com/mattgwwalker/msg-extractor

import extract_msg

def main():

    # Using message module to parse Microsoft Outlook message files.
    msg = extract_msg.Message("./sample_files/sample1_a.msg")

    # Retrieving summary of message
    print("----------------SUMMARY OF MESSAGE-----------------",'\n')
    msg.dump()

    # Retrieving header information
    msg_header = msg.header
    print("----------------HEADER INFORMATION-----------------",'\n', msg_header)
      
    # Saves the message body and attachments in given path
    msg.save(customPath = "/home/kajol/LawFact/Email_Forensics/output/")

    # Saves only attachments in the given path
    save_msg = msg.save_attachments(customPath = "./output/attachments")
   
if __name__ == "__main__":
    main()
