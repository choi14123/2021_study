a = []
for i in range(5):
    b = int(input(""))
    if b <= 40:
        b = 40
    a.append(b)
print(int(sum(a) / 5))