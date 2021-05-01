num = int(input(""))
for i in range(num):
    A, B = map(int, input().split())
    print("Case #%d: %d"%(i+1, A+B))