a = int(input())

for i in range(a):
    b = input()
    score = 0
    sumScore = 0
    for j in b:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)