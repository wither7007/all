num=input("enter no of files to be created:")
items =[]
for i in range(1,(int(num)+1)):
    items.append(i)
for item in items:
    open("%s_file.txt" % item, "a").close()
