import sys
output = ""
for a in sys.argv:
    print(a)

target = sys.argv[1]
print(f" arg one is {target}")
with open(target) as f:
    for line in f:
        if not line.isspace():
            output += line

f = open(target, "w")
f.write(output)
