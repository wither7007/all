from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE, ST_ATIME
import os
import sys
import time
import datetime
import re
from tabulate import tabulate
numlists = ["5","50","7","51","87","97","53"]
sorted(numlists)
numlists
sorted(results)
list(map(int,results))
list(map(str,results))
list(map(int*3,results))
list(map(a*3,results))
list(map(lambda a: a*3,results))
list(map(lambda a: a*30,results))
fi
import re
fi.sort(key=lambda f: int(re.sub('\D', '', f)))
line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line )
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."
dsteir_path = sys.argv[1] if len(sys.argv) == 2 else r"."

data = list(os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
d=data[1]
str1 = "3158 reviews"
str1= os.listdir()[1]
print (re.findall('#\d+', str1 ))
d.index('e')
# all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

data = list(os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
b=[e for e in a if e.startswith('a')]
os.getcwd()
os.chdir(r'c:\you')
os.getcwd()
a=next(os.walk('.'))[1]
a
b=[e for e in a if 'wy' in e]
b=[e for e in a if  re.search(r"w",e]
b

import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+", xx)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))
"jim".split()
data[1].split(" ")
' '.join(data[1].split(" "))

list='''shoat
xxxxw
tubal
eclat
1111111111
olam
aaaa
stat
bbbbbbbb
gnar
babai
scoad
scrap'''.split('\n')
mlist = sorted(w, key=lambda x: x[-1:])
mlist = sorted
h=(w, lambda x: x[-1:])

' '.join(list)
list2='''shoat
tubal
eclat
olam
stat
gnar
babai
scoad
scrap'''.replace('\n', ' ')
v='''I have a list of words where I want to sort based on their last (2,3) letters. In other words if we say (Sort by Words ending with)

Following things I already tried aren't working for me. Maybe it requires a single more argument or needs a separate method for sorting.'''
w=v.split()
import subprocess
longStr = r''

subprocess.call(['Get-ChildItem'], shell=True)
import subprocess
import sys
p = subprocess.Popen(['powershell.exe', 'pss.ps1'], stdout=sys.stdout)
_