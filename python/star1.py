a = int(input(""))

for i in range(a, 0, -1):
    print(" " * (a - i) + "*" * i)

for i in range(0, a):
    print(" " * (a - i) + "*" * i)
