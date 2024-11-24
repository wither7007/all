# reads ipython sqlite datbase and exports to mypy text file
import sqlite3

db = "conn=sqlite3.connect('C:/Users/jayst/.ipython/profile_default/history.sqlite')"
conn = sqlite3.connect("C:/Users/jayst/.ipython/profile_default/history.sqlite")
c = conn.cursor()
fileName = r"c:\projects\sqllite\ipy"
f = open(fileName, "w", encoding="utf-8")
ip = c.execute("SELECT source from history")
mapping = dict.fromkeys(range(32))
for row in ip:
    # print(len(str(row)))
    myRow = row[0].translate(mapping)
    if len(myRow) != 0:
        print(myRow.strip(), file=f)
    # print('-----------------------------------------------------------')


# c.execute("SELECT name FROM sqlite_master WHERE type='table'")
# f=open('sql', 'w')
# print(c.fetchall(), file=f)
# f.close()
# c.execute("PRAGMA table_info()").fetchall()
# print(c.fetchall())
# for row in c.execute("PRAGMA table_info('history')").fetchall():
#     print(row)
# h=c.fetchall()
# print(c.fetchall())
