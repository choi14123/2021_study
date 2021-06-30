from heapq import heappush, heappop

Inf = 100000000
vn, en = map(int, input().split())
E = [ [] for _ in range(vn) ]
for _ in range(en):
    f, t, w = map(int, input().split())
    E[f-1].append( (w, t-1) )
    E[t-1].append( (w, f-1) )

visited = [ False ]*vn
d = [ Inf ]*vn
d[0] = 0
pq = [ (0, 0) ]

sum = 0
while len(pq) != 0:
    u = heappop(pq)
    if visited[u[1]]: continue
    print(u)
    sum += u[0]
    visited[u[1]] = True
    for e in E[u[1]]:
        if visited[e[1]]: continue
        if d[e[1]] > e[0]:
            d[e[1]] = e[0]
            heappush(pq, (e[0], e[1]))

print(sum)
