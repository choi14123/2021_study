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

def _mergeSort(v, a, b):
    c = (a+b) // 2
    _selectionSort(v, a, c)
    _selectionSort(v, c+1, b)
    t = []
    i, j = a, c+1
    while i <= c and j <= b:
        if v[i] <= v[j]:
            t.append(v[i])
            i += 1
        else:
            t.append(v[j])
            j += 1
    while i <= c:
        t.append(v[i])
        i += 1
    while j <= b:
        t.append(v[j])
        j += 1
    for k in range(len(t)):
        v[a+k] = t[k]

def mergeSort(v):
    _mergeSort(v, 0, len(v)-1)

n = int(input("n의 값을 입력 :"))
v = [ random.randint(1, 1000000) for _ in range(n) ]
ts = time.time()
mergeSort(v)
et = int((time.time() - ts) * 1000)
print("경과 시간 : {}ms".format(et))
