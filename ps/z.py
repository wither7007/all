#good import unzip a file
# app.py
import sys

from zipfile import ZipFile
filename = sys.argv[1]
with ZipFile(filename, 'r') as zipObj:
    # Extract all the contents of zip file in current directory
    zipObj.extractall()
