import glob
from operator import itemgetter
import os
import sys
import tabulate
import datetime

li = """His Discourse on Inequality and The Social Contract are cornerstones in modern political and social thought. Rousseau's sentimental novel Julie, or the New Heloise """.split()

v = ["1", "2", "-3"]
[x[1] for x in v]


def fnc(n):
    return "{:,}".format(n)


def cti(o):
    # o=os.path.getctime("file.txt")
    dti = datetime.datetime.fromtimestamp(o)
    return dti.strftime("%x")


def stn(p):
    print(p, type(p))
    return int(p)


tl = []
files = glob.glob("*.*")
for f in files:
    tl.append(["\t", f"{f}", f"{os.stat(f).st_size}", f"{cti(os.stat(f).st_atime)}"])
    # print(f"{f} \t {fn(os.stat(f).st_size)}")
tls = sorted(tl, key=lambda e: stn(e[2]))
print(tabulate.tabulate(tls))
print("done")
