from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE, ST_ATIME
import os
import sys
import time
from datetime import datetime

# Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."

# all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
# data = ((stat[ST_MTIME],stat[ST_ATIME] path) for stat, path in data if S_ISREG(stat[ST_MODE]))
data = (
    (stat[ST_MTIME], stat[ST_ATIME], path)
    for stat, path in data
    if S_ISREG(stat[ST_MODE])
)
now = datetime.now()
for cdate, adate, path in sorted(data):
    print("-" * 10)
    k = time.ctime(cdate)
    print(k)
    l = f"{now:%d-%B-%Y}"

    print(f" l is {l}\n")
    # print(time.ctime(cdate), time.ctime(adate), os.path.basename(path))


"""
length_list = [len(element) for row in a for element in row]
ll = [len(element) for row in a ]
a="Born in Maida Vale, London, Turing was raised in southern England. He graduated at King's College, Cambridge, with a degree in mathematics." 
b=a.split(' ')
k=[1,2,3]
c=list(map(lambda n:n+ " this",b))
' '.join(c)
class check:
    def __init__(self):
        print("Address of self = ",id(self))
 
obj = check()
print("Address of class object = ",id(obj))
 
# this code is Contributed by Samyak Jain


"""
