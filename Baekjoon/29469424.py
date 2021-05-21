A, B, C = list(map(int, input().split()))
money = 0
if(C <= B):
    money = -1
else:
    money = A // (C - B) + 1
print(money)