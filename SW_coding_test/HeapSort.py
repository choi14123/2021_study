import heapq
import random
import time

def heapSort(v):
    heapq.heapify(v)
    t = [ heapq.heappop(v) for _ in range(len(v)) ]
    return t

n = int(input(" n : "))
v = [ random.randint(1, 1000000) for _ in range(n) ]
ts = time.time()
v = heapSort(v)
et = int((time.time() - ts) * 1000)
print("경과 시간(Elapsed time) : {}ms".format(et))
