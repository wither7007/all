import os 
import sys
    
# path 
#path = 'D:/Pycharm projects / GeeksForGeeks'
path = 'c:/temp/python'
    
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
try: 
#    os.mkdir(path) 
    n = len(sys.argv)
    print("Total arguments passed:", n)
for i in range(1, n):
    print(int(sys.argv[i]))
except OSError as error: 
    print(error)  
