from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE, ST_ATIME
import os
import sys
import time
import datetime
import my
from tabulate import tabulate

b = dir(os)
out = [b[i : i + 1] for i in range(0, len(b), 4)]
# print(out)
my.col_print(b)
print("done")
