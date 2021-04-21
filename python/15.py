
first_num = int(input("시작 정수를 입력하세요"))
last_num = int(input("끝 정수를 입력하세요"))
hap = []
for i in range(last_num - 1 ) :
    hap.append(first_num + i)


print("{} 에서 {} 까지 정수의 합 : {}  ".format(first_num, last_num, sum(hap)))

