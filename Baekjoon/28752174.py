import sys
cases = int(input())

for i in range(cases):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)