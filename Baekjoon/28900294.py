a = int(input())
hap = list(map(int, input().split()))
max_score = max(hap)

avg = []
for score in hap :
    avg.append(score/max_score *100)
test_avg = sum(avg)/a
print(test_avg)
