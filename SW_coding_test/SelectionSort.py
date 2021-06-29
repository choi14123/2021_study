import time
import random

def _selectionSort (v, a, b):
    for i in range(a, b):
        min = i
        for j in range(i+1, b+1):
            if v[min] > v[j]: min = j
        v[i], v[min] = v[min], v[i]

def selectionSort(v):
    _selectionSort(v, 0, len(v)-1)

n = int(input("n의 값을 입력 :"))
v = [ random.randint(1, 1000000) for _ in range(n) ]
ts = time.time()
selectionSort(v)
et = int((time.time() - ts) * 1000)
print("경과 시간 : {}ms".format(et))
