# app.py

from zipfile import ZipFile

with ZipFile('profile-card-hover.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
