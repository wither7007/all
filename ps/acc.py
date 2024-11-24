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
    print(f"{key}, {c(value)}")


def c(x):
    try:
        return time.ctime(x)
    except:
        print("An exception occurred")


def f(x):
    try:
        return x / 0
    except:
        print("An exception occurred")


if __name__ == "__main__":

    d = {"A": 0, "B": 1, "C": 2}

    for k, v in d.items():
        d[k] = f(v)
