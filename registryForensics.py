#!/usr/bin/env python

#Reference  : https://github.com/mkorman90/regipy
#

import regipy

#fIn = raw_input("Submit the File for Analysis : ")

#Initiate the Registry Hive Object
reg = regipy.registry.RegistryHive('./123NTUSER.DAT')

#General Information About Registry Under Analysis
print("Registry Header : %s\n" %reg.header)
print("Registry Hive Type : %s\n" %reg.hive_type)
print("Registry Name : %s\n" %reg.name)

#Iterate Recursively Over the Entire Hive from ROOT Key
for item in reg.recurse_subkeys(as_json=True):
    print(item)

#Iterate Over a Key and Get all Subkeys and Their Modification Time
for sk in reg.get_key('\Software').iter_subkeys():
    #print(sk.name, convert_wintime(sk.header.last_modified).isoformat())
    print(sk.name)

#Get the Values of a Key
#reg.get_key('Software\Microsoft\Intenet Explorer\BrowserEmulation').get_values(as_json=True)

#Run All Relevant Plugins for a Specific Hive
#reg = RegistryHive('')
#run_relevant_plugins(reg, as_json=True)



