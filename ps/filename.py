import os
 
# directory name from which
# we are going to extract our files with its size
import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
path = "c:\\all"
 
# Get list of all files only in the given directory
fun = lambda x : os.path.isfile(os.path.join(path,x))
files_list = filter(fun, os.listdir(path))
 
# Create a list of files in directory along with the size
size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]
# Iterate over list of files along with size
# and print them one by one.
for f,s in size_of_file:
    print("{} : {}mb".format(f, round(s/(1024*1024),3)))
