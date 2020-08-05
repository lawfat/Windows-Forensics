#!/usr/bin/env python3

#Reference: https://github.com/williballenthin/python-evtx

import Evtx.Evtx as evtx
import Evtx.Views as e_views

def main():

    # Create a file for saving the output
    with open("EventlogAnalysis.txt","w") as file1:

        # Open evtx file using Evtx and convert it into XML.
        with evtx.Evtx("/home/kajol/LawFact/EventLogAnalysis/logs/System.evtx") as log:
            file1.write(e_views.XML_HEADER)
            file1.write("<Events>")
        
            # Get each of the records from this evtx file.
            for record in log.records():
                file1.write(record.xml())
            file1.write("</Events>")

if __name__ == "__main__":
    main()

