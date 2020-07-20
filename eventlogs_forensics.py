#!/usr/bin/env python3

#Reference: https://github.com/williballenthin/python-evtx

import Evtx.Evtx as evtx
import Evtx.Views as e_views

def main():

    # Open evtx file using Evtx and convert it into XML.
    with evtx.Evtx("/home/kajol/LawFact/EventLogAnalysis/logs/System.evtx") as log:
        print(e_views.XML_HEADER)
        print("<Events>")
        
        #Get each of the records from this evtx file.
        for record in log.records():
            print(record.xml())
        print("</Events>")

if __name__ == "__main__":
    main()

