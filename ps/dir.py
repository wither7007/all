import os
import re
import clipboard
clipboard.copy("abc")  # now the clipboard content will be string "abc"

folder = r"c:\all"
myFiles = os.listdir(folder)
# for count, filename in enumerate(os.listdir(folder)):
#     print(count, filename)


def filter_fun(list1):
    # Search data based on regular expression in the list
    return [val for val in list1
            if re.search(r'jpg', val)]


# print(filter_fun(myFiles))

ff = filter_fun(myFiles)
f1 = ''
for i in ff:
    f1 += '<img src="' + i+'">\n'
print(f1)

clipboard.copy(f1)
# <img src="" alt="">
