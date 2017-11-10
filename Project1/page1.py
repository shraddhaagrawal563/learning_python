# -*- coding: utf-8 -*-
import os
import shutil
import time
from time import gmtime, strftime

path= os.getcwd()
print("current working directory is:", path)
path2=path
cwd=path+'\\input'
os.chdir(cwd)
print("current path inside input folder:", cwd)
files= os.listdir()
for file in files:
    print(file)
    
files= os.listdir()
for i in files:
    tm=strftime("%Y-%m-%d-%H-%M-%S", gmtime())
    filenm="backup"+i+tm
    print(filenm)

outadd = path2+'\\backupraw'
print("outadd: ",outadd)    
os.chdir(outadd)  
inadd = cwd
#open(input, 'w').close()
print("inadd: ",inadd)
print("CWD: ",os.getcwd())
print("LINE 30: Changing CWD to input...")
os.chdir(inadd)
print("CWD after change: ",os.getcwd())
files= os.listdir()
for i in files:
    print("Original file: ",i)
    bknm="backup_"+tm+"_"+i
    print("Backup file name: ",bknm)
    infile=inadd+"\\"+i
    print("Original file path: ",infile)
    outfile=outadd+"\\"+bknm
    print("Backup file path: ",outfile)
    shutil.copy2(infile,outfile) #copy2 function inside shutil module



    
