count = int(input(“입력하는 학생수가 총 몇 명인가요? : “)
print(“학생의 이름과 시험 점수를 차례대로 입력하세요!”)
scores = list()
num = 1


# 이름 및 점수 입력
while num <= count:
print(num, '번째 학생 =====') _______________________________
_______________________________
_______________________________
_______________________________ num += 1

# 딕셔너리로 타입 전환
___________________________


# 학생 이름 및 점수 출력
flag = True
while flag:
wanted = input('어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요. : ')
if wanted in scores_dict:
print(wanted, '학생의 점수 : ', scores_dict[wanted])
flag = False
print('프로그램을 종료합니다.')
else:
print('찾는 학생(', wanted, ')의 점수가 존재하지 않습니다.')
