import os
import stat
import time


def get_file_event_time():
    filePath = r"C:\all\ps\getStat.ps1"
    print(filePath)
    accessTimesinceEpoc = os.path.getatime(filePath)
    accessTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(accessTimesinceEpoc))
    print("File Last Access Time looking for : " + accessTime)


get_file_event_time()
