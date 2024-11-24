from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE, ST_ATIME
import os
import sys
import time
from datetime import datetime
import datetime
import tabulate

today = datetime.date.today()
print(today)


def cti(o):
    # o=os.path.getctime("file.txt")
    dti = datetime.datetime.fromtimestamp(o)

    return dti.strftime("%x").strip('\u200e')

dir_path=r"."
# dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."

data = list(os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
# data = ((stat[ST_MTIME],stat[ST_ATIME] path) for stat, path in data if S_ISREG(stat[ST_MODE]))
data = list(
    (stat[ST_MTIME], stat[ST_ATIME], path)
    for stat, path in data
    if S_ISREG(stat[ST_MODE])
)
tar=[]
for cdate, adate, path in sorted(data):

    tar.append([f"{os.path.basename(path)} ", f"{cti(cdate)} {cti(adate)}"])

print(tabulate.tabulate(tar))