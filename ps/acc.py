import os
import stat
import time

from pydantic import FilePath


def get_file_event_time():
    filePath = r"C:\all\ps\getStat.ps1"
    print(filePath)
    accessTimesinceEpoc = os.path.getatime(filePath)
    accessTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(accessTimesinceEpoc))
    print("File Last Access Time looking for : " + accessTime)


get_file_event_time()


p = pathlib.Path("test")
p.write_text("test")
print(p.stat())
x = p.stat()
y = enumerate(x)
print(list(y))


def stat_to_json(fp: str) -> dict:
    s_obj = os.stat(fp)
    return {k: getattr(s_obj, k) for k in dir(s_obj) if k.startswith("st_")}


n = stat_to_json(filePath)
for key, value in n.items():
    print(f"{key}, {value}")
