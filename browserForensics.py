#!/usr/bin/env python2

#References: https://likegeeks.com/python-sqlite3-tutorial/#List-tables
#            http://zetcode.com/db/sqlitepythontutorial/
#pip install db-sqlite3

#Import Sqlite3 Module and Pandas
import sqlite3
import time                 #Used to convert epoch time to real datetime

def listTables(cursorObj):
    #Show the Available Tables
    #print("\n[*] Listing Available Tables ........")
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tableList = cursorObj.fetchall()
    print("List of Tables : %s" %tableList)
    '''for line in tableList:
        print line[0]'''
    return len(tableList),tableList

def listColumns(cursorObj,getTable_name):
    #Show the Colums from Tables
    #getTable_name = raw_input("\nEnter the Table Name for Analysis : ")
    print("\n[*] Listing Columns from %s" %getTable_name)
    readColumn_names = "SELECT name FROM PRAGMA_TABLE_INFO ('" + getTable_name[0] + "')"
    #print readColumn_names
    cursorObj.execute(readColumn_names)
    columnList = cursorObj.fetchall()
    print("List of Columns : %s" %columnList)
    '''for line in columnList:
        print(line[0])'''
    return getTable_name[0],columnList

def columnValues(cursorObj,tableName,columnList):

    #Create comma-separated Column Names for Crafting SQL Query
    sql_query = "SELECT * FROM " + tableName
    #print sql_query
    cursorObj.execute(sql_query)
    #Fetch the Results Obtained by SQL Queries
    result = cursorObj.fetchall()
    #Print the Results
    print("\n")
    for line in result:
        print(line)

    fOut = open('output.txt','a')
    string1 = "[+] " + "Printing Contents of " + tableName + "\n" 
    fOut.write(string1)
    for line in result:
        fOut.write(str(line) + "\n")
    fOut.close()
    return

def epoch2datetime(epochTime):
    return time.ctime(float(str(epochTime)))

def main():

    #Read the Input File for Analysis
    fIn = raw_input("Please Submit the .sqlite File for Analysis : ")

    #Create Connection
    con = sqlite3.connect(fIn)

    #Create a Cursor Object to call execute() function to execute any SQL queries
    cursorObj = con.cursor()

    numberTables,tableList = listTables(cursorObj)

    count = 0

    while(count < numberTables):

        tableName,columnList = listColumns(cursorObj,tableList[count])

        columnValues(cursorObj,tableName,columnList)
        
        count += 1

    #Close the Connection 
    con.close()

if __name__=='__main__':
    main()
