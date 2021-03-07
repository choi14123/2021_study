x = [5, 1, 3, 7, 2, 9]

a = len(x)

for i in range(0, a - 1):

    min_idx = i

    for j in range(i + 1, a):

        if x[j] < x[min_idx]:

            min_idx = j

    x[i], x[min_idx] = x[min_idx], x[i]


 

print(x)

