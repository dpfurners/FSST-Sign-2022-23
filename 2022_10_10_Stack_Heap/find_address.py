import sys

sys.setrecursionlimit(10)

z = 10
y = 12
print(f"Variable in the Function Function:\nz is located at: {hex(id(z))}\ny is located at: {hex(id(y))}")


def recursive(x):
    print(hex(id(x)))
    return recursive(x + 1)


print(hex(id(__name__)))


try:
    recursive(12)
except RecursionError:
    pass
