# -*- coding: utf-8 -*-
import platform
import sys
import sqlite3
print("operating system is:", platform.platform()) #gives os platform details

print("\noperating system details:")
print("system:",platform.system())
print("release:",platform.release())
print("version:",platform.version())

print("python version:", sys.version) #gives python version

con = sqlite3.connect('test.db') #if not present then create test.db
cur = con.cursor()    
cur.execute('SELECT SQLITE_VERSION()') #gives sqlite version
print("\ndatabase version is:")
data = cur.fetchone() #fetches one row from result set at a time
print ("SQLite version:", data)                
con.close()