from bisect import bisect_left

s = tuple(map(int, input().split()))
seq = [s[0]]

for i in range(1, len(s)):
    if seq [-1] < s[i] :
        seq.append(s[i])
    else:
        idx = bisect_left(seq, s[i])
        seq[idx] = s[i]

print(len(seq))
