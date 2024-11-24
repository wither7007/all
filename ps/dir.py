import datetime
import os
import sys
folder=r"c:\you\alb"
path = r"C:\projects\gpython\a.ps1"
for count, filename in enumerate(os.listdir(folder)):
  print(filename)
  m_time = os.path.getmtime(path)
  print(m_time)




'''
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        print(full_path) 

import os 
path = "/projects"
dirct = os.listdir(path) 
print("Files and directories:") 
print(dirct)
import os
absp = os.path.abspath(os.getcwd())
print("Full path: " + absp)
print("Directory Path: " + os.path.dirname(absp))

---------------------------
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
'''