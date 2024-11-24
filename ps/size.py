# list sizes directory
import os
import math
import sys

print("\nName of Python script:", sys.argv[0])
# dir_name = sys.argv[1]
dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


# Get list of all files only in the given directory
list_of_files = filter(
    lambda x: os.path.isfile(os.path.join(dir_path, x)), os.listdir(dir_path)
)
# Create a list of files in directory along with the size
files_with_size = [
    (file_name, os.stat(os.path.join(dir_path, file_name)).st_size)
    for file_name in list_of_files
]
# Iterate over list of files along with size
# and print them one by one.
files_with_size.sort(key=lambda e: e[1])
for file_name, size in files_with_size:
    print(convert_size(size), " -->", file_name)
