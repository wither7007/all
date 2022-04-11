from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE
import os, sys, time

# Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."

# all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_MTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))


"""
a="Born in Maida Vale, London, Turing was raised in southern England. He graduated at King's College, Cambridge, with a degree in mathematics." 
b=a.split(' ')
k=[1,2,3]
c=list(map(lambda n:n+ " this",b))
' '.join(c)

"""
