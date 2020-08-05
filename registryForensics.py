#!/usr/bin/env python

#Reference  : https://github.com/mkorman90/regipy
#

import regipy

#fIn = raw_input("Submit the File for Analysis : ")

#Initiate the Registry Hive Object
reg = regipy.registry.RegistryHive('./123NTUSER.DAT')

# Creating file for saving output
with open('RegistryAnalysis.txt', 'w') as file1:

    #General Information About Registry Under Analysis
    file1.write("REGISTRY HEADER : %s\n" %reg.header)
    file1.write("REGISTRY HIVE TYPE : %s\n" %reg.hive_type)
    file1.write("REGISTRY NAME : %s\n" %reg.name)
    file1.write("\n")

    #Iterate Recursively Over the Entire Hive from ROOT Key
    for item in reg.recurse_subkeys(as_json=True):
        file1.write("SUBKEYS : %s\n" %item)
        file1.write("\n")

    #Iterate Over a Key and Get all Subkeys 
    for sk in reg.get_key('\Software').iter_subkeys():
        file1.write("Subkey Name : %s\n" %sk.name)

    #Get the Values of a Key
    #reg.get_key('Software\Microsoft\Internet Explorer\BrowserEmulation').get_values(as_json=True)

    #Run All Relevant Plugins for a Specific Hive
    #reg = RegistryHive('')
    #run_relevant_plugins(reg, as_json=True)



