from heapq import heappush, heappop

def getRoot(S, k):
    if S[k] == k: return k
    S[k] = getRoot(S, S[k])
    return S[k]

Inf = 100000000
vn, en = map(int, input().split())
E = [ ]
for _ in range(en):
    f, t, w = map(int, input().split())
    E.append( (w, f-1, t-1) )

S = [ i for i in range(vn) ]
E.sort()

sum = 0
for e in E:
    u, v = e[1], e[2]
    ur, vr = getRoot(S, u), getRoot(S, v)
    if ur == vr: continue
    S[vr] = ur
    sum += e[0]

print(sum)
