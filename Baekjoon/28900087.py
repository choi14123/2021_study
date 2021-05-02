hap = []

for i in range(10) :
    a = int(input(""))
    hap.append(a % 42)
hap = set(hap)
print(len(hap))