import sys
from num2words import num2words


numbers = list(map(lambda i: i * 10, [i for i in range(1, 6)]))
def dd():
    print(dir())

def fh(d):
    print(d, "\n")
    u = dir(os)
    print([x for x in u if u[0] == "_"])
    # print(f"\nu is {u}\n")


#import ctypes
import ctypes

# variable declaration
val = 20

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)

fh("sys")
answer = 0
sys.exit()


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n - 1)) + (fib(n - 2))


for a in range(0, 20):
    print(f"{a}: {fnc(fib(a))}")


def fnc(n):
    return "{:,}".format(n)


def fac(n):
    return 1 if (n == 0 or n == 1) else n * fac(n - 1)


fac(5)
# q = 2**256
# print(num2words(fac(20)))
# print(num2words(q))
# print("*" * 30)
# print(fnc(q))
sys.exit()


def fact(n):
    if n == 1:
        return n
    n = n - 1
    print(n)
    # print(f"n is {n} and answer is: {answer}")
    n += fact(n)


fact(3)
sys.exit()

# list1=list(str(n))
# list2=list(str(o))
# print(list1, list2)
# return set(list1)=setlist2
# # return tuple(n)==tuple(set(o))

a = 123
b = str(a)
c = [char for char in b]


def eq(n):
    n = list(str(n))
    return len(n) == len(set(n))


chars = "aeiou"
c = 0
for x in range(0, len(chars)):
    print(chars[x])
    c += 1
