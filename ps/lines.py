a_file = open("sample.txt", "r")
#get list of lines

lines = a_file.readlines()
a_file.close()

new_file = open("sample.txt", "w")
for line in lines:
    if line.strip("\n") != "line1":
#Delete "line2" from new_file

        new_file.write(line)

new_file.close()
