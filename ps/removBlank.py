import sys
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
print(dir_path)
# sys.exit()
output=""
with open(dir_path) as f:
    for line in f:
        if not line.isspace():
            output+=line
            
with open(dir_path,"w") as outfile:
    outfile.write(output)