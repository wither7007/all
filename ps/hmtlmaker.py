import os
import re
import clipboard
import touch
from pathlib import Path


folder = r"c:\you\js"
myFiles = os.listdir(folder)
newFolder = r"c:\you\js\xyz"
fp = open(newFolder, 'x')
fp.close()
myFiles2 = os.listdir(folder)
# for count, filename in enumerate(os.listdir(folder)):
#     print(count, filename)
list_difference = [element for element in myFiles2 if element not in myFiles]
print(list_difference)
touch.touch([list_difference[0]])
touch.touch('xyz')


Path(newFolder).touch()
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
