def dfs(mapk, visit, y, x):
    visit[y][x] = True
    n = len(mapk)
    m = len(mapk[0])
    dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
    for k in dxy:
        ny = y + k[0]
        nx = x + k[1]
        if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
        if visit[ny][nx] == True or mapk[ny][nx] == 0: continue
        dfs(mapk, visit, ny, nx)

def bfs(mapk, visit, y, x):
    q = [ (y, x) ]
    n = len(mapk)
    m = len(mapk[0])
    dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
    while not len(q) == 0:
        u = q.pop(0)
        visit[u[0]][u[1]] = True
        for k in dxy:
            ny = u[0] + k[0]
            nx = u[1] + k[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if visit[ny][nx] == True or mapk[ny][nx] == 0: continue
            q.append((ny, nx))

n, m = map(int, input().split())
mapk = [ ]
for i in range(n):
    line = [ ]
    s = input()
    for k in s:
        if k == '1': line.append(1)
        else: line.append(0)
    mapk.append(line)

visit = [ [ False ]*m for _ in range(n) ]

island = 0

for y in range(n):
    for x in range(m):
        if visit[y][x] == False and mapk[y][x] == 1:
            island += 1
            bfs(mapk, visit, y, x)

print(island)
