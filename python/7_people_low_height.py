ke = []
for i in range(9):
    a = int(input(""))
    ke.append(a)


max1 = max(ke)
ke.remove(max1)
max2 = max(ke)
ke.remove(max2)
ke.sort()
sum_ke = sum(ke)


if sum_ke <= 100 :
    for i in range(7) :
        print(ke[i])
