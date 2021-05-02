num = int(input(""))
han = 0

for n in range(1, num + 1):
    if n <= 99:
        han += 1

    else:
        num = list(map(int, str(n)))
        if num[0] - num[1] == num[1] - num[2]:
            han += 1
print(han)