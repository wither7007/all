#!/usr/bin/python3
import subprocess
o = subprocess.check_output(['node', '--version'], text = True)
print('You are using Node ' + o)
