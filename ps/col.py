import pandas as pd
import os

# d = [["Mark", 12, 95],
#      ["Jay", 11, 88],
#      ["Jack", 14, 90]]

folder = "."
# files = list(enumerate(os.listdir(folder)))
files2 = list(os.listdir(folder))
x = 3


def final_list(test_list, x): return [test_list[i:i+x]
                                      for i in range(0, len(test_list), x)]


output = final_list(files2, x)

# print('The Final List is:', output)
# for count, filename in enumerate(os.listdir(folder)):
#     print(filename)

df = pd.DataFrame(output, columns=['', '', ''])
print(df)
