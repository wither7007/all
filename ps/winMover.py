#cool kludge to create script to move files
#important 
#sorting directory by number
import random
import glob
import re
import touch
import os
import sys
def max_num(n, o):
    result = []
    for p in range(n, o):
        if o % p == 0:
            print(f"o is {o} and p is {p} and factor is {o%p}")
            result.append(p)
            print(result)
    return result

    
    
import sys

print('This message will be displayed on the screen.')

with open('filename.ps1', 'w') as f:
    for k in sc:
        print(k, file=f)
import glob
import re
reg='#'
import sys
sc=[]
for file in  glob.glob('*.*'):
    if re.search(reg, file):
        sc.append(f"mv \'{file}\' \'{re.sub('.*#', '', file)}\'")

print(f'glob is {test_list}')
r = max_num(1, 328)
aa=list(range(0,10))
func = lambda x: int(str(x)[len(str(x))-1])

def ri():
    return random.randint(0,10000)
t

mm=[]
for a in range(0,20):    mm.append([ri(), ri()])
func2=lambda x: x[1]
import re

test_list = ["Gfg34", "is67", "be3st", "f23or", "ge9eks"]
test_list= glob.glob('*.*')
print("The original list is : " + str(test_list))

test_list.sort(key=lambda test_string : list( map(int, re.findall(r'\d+', test_string)))[0])
for a in test_list:
    print(a)
    Path(a).touch()
#https://appdividend.com/2021/02/18/how-to-implement-touch-file-in-python/
print("Strings after numerical Sort  : " + str(test_list))
#https://www.geeksforgeeks.org/python-sort-given-list-of-strings-by-part-the-numeric-part-of-string/
from pathlib import Path

dir_path=(r'c:\temp')
data = list(os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
Path('duh').touch()
def glbo():
    a=dir()
    print(a)
glbo()
import re
  
# initializing string
test_str = 'geeksforgeeks'
  
# printing original String
print("The original string is : " + str(test_str))
  
# using sub() to perform substitutions
# ord() for conversion.
res = (re.sub('.', lambda x: r'\u % 04X' % ord(x.group()), test_str))
  
# printing result 
print("The unicode converted String : " + str(res)) 