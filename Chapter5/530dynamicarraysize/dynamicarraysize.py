import sys
data = []
n = 26
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {0:4d}'.format(a, b))
    data.append(None)