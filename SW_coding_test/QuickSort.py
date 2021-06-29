import time
import random

def partition(v, a, b):
    pivot = v[b]
    i, j = a, b-1
    while i <= j:
        if v[i] <= pivot: i += 1
        else:
            v[i], v[j] = v[j], v[i]
            j -= 1
    v[i], v[b] = v[b], v[i]
    return i

def _quickSort(v, a, b):
    if b <= a: return
    c = partition(v, a, b)
    _quickSort(v, a, c-1)
    _quickSort(v, c+1, b)

def quickSort(v):
    _quickSort(v, 0, len(v)-1)

n = int(input("n : "))
v = [ random.randint(1, 1000000) for _ in  range(n) ]
ts = time.time()
quickSort(v)
et = int((time.time() - ts)* 1000)
print("경과 시간 : {}ms".format(et))
