def _histogram(h, a, b):
    if a == b: return h[a]
    c = (a+b)//2
    left = _histogram(h, a, c)
    right = _histogram(h, c+1, b)
    max = left
    if max < right: max = right
    minlen, len = min(h[c], h[c+1]), 2
    if max < minlen * len: max = minlen * len
    i, j = c-1, c+2
    while i >= a and j <= b:
        if h[i] > h[j]:
            if h[i] < minlen: minlen = h[i]
            len, i = len+1, i-1
        else:
            if h[j] < minlen: minlen = h[j]
            len, j = len+1, j+1
        if max < minlen*len: max = minlen*len
    while i >= a:
        if h[i] < minlen: minlen = h[i]
        len, i = len+1, i-1
        if max < minlen*len: max = minlen*len
    while j <= b:
        if h[j] < minlen: minlen = h[j]
        len, j = len+1, j+1
        if max < minlen*len: max = minlen*len
    return max

def histogram(h):
    return _histogram(h, 0, len(h)-1)


h = tuple(map(int, input().split()))

print(histogram(h))
