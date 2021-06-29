def perm(v, r, s = []):
    if r == 0:
        print(s)
        return
    for x in v :
        if x in s:continue
        perm(v, r - 1, s + [x])

v = ["홍길동", "성춘향", "이몽룡", "변사또"]
r = 3
perm(v, 3)
