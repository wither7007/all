import sys
import os

a = range(1, 1000)
print(a)
for name, value in os.environ.items():
    print(f"{name}: {value}")
