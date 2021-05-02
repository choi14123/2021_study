list_a = []
for i in range(9) :
    a = int(input(""))
    list_a.append(a)

print(max(list_a))
print(list_a.index(max(list_a)) + 1)