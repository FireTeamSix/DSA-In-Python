from time import time


def compute_average(n):
    """Perform n appends to an empty list and returns time elapsed"""
    
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

print(compute_average(100000000))