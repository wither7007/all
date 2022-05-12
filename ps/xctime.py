from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE, ST_ATIME
import os
import sys
import time
from datetime import datetime
import datetime

today = datetime.date.today()
new_year = datetime.date(2019, 1, 1)
print(new_year)


def cti(o):
    # o=os.path.getctime("file.txt")
    dti = datetime.datetime.fromtimestamp(o)
    return dti.strftime("%x")


# import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
# print("Created: %s" % time.ctime(os.path.getctime("file.txt")))
# o=os.path.getctime("trans.py")
# n=datetime.now()
# print(f'{n:%Y-%m-%d %H:%M}')
# dti = datetime.datetime.fromtimestamp(o)
# dtis = dti.strftime( "%Y - %m - %d  %H : %M : %S")
# dtis = dti.strftime( "%x")

# Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."

data = list(os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
for a in data:
    print(a)
# regular files, insert creation date
# data = ((stat[ST_MTIME],stat[ST_ATIME] path) for stat, path in data if S_ISREG(stat[ST_MODE]))
data = list(
    (stat[ST_MTIME], stat[ST_ATIME], path)
    for stat, path in data
    if S_ISREG(stat[ST_MODE])
)
for cdate, adate, path in sorted(data):
    # print("-" * 10)
    # k = time.ctime(cdate)
    # print(f"k is {k}")
    # l = f"{now:%d-%B-%Y}"

    # print(f" l is {l}\n")
    print(
        f"\t{os.path.basename(path)} {len(os.path.basename(path))} ---> \t\t create date: {cti(cdate)} access date: {cti(adate)}"
    )
    # (time.strftime("%m/%d/%Y:%M"), time.ctime(cdate))
    # print(cti(cdate))

# ct = cdate.strftime("%d/%m/%Y")
