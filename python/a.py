count = int(input("입력하는 학생수가 총 몇 명인가요? : "))
print("학생의 이름과 시험 점수를 차례대로 입력하세요!")

t1 = tuple()
t2 = tuple()

scores = list()
l_name = list()
num = 1

while num <= count:
    print(num, '번째 학생 =====')
    t1 = ( input("* 사람 : "))
    l_name .append(t1)
    t2 = int(input("* 성적 : "))
    scores.append(t2)
    num += 1
    
scores_dcit = dict(zip(l_name, scores))


flag = True

while flag:
    wanted = input("어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요 : ")

    if wanted in scores_dcit:
        print(wanted, "학생의 점수 : ", scores_dcit[wanted])
        flag = False
        print("프로그램을 종료합니다.")
    else:
        print("찾는 학생(", wanted, ") 의 점수가 존재하지 않습니다. ")

