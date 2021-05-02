n = int(input())
for i in range(n):
    A, B = input().split()
    for j in range(len(B)):
        print(B[j]*int(A), end='')
    print()

