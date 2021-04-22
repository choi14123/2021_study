# 이수학점 time, 평점 grade 로 리스트 선언
time = []
grade = []

# 함수 선언
def grade_ok ():
    if sum(time) >= 140 and avg_grade >= 2.5 : #제어문으로 졸업가능 한지 확인
        print("졸업이 가능합니다.")
    else:
        print("졸업이 어렵습니다.")

#반복문 이용해 이수학점, 총점 입력받기
for i in range(1,5):
    for n in range(1,3):
        a = float(input("{}학년 {}학기 이수학점을 입력하세요 :".format(i,n)))
        if 0 <= a <= 30 : #제어문으로 이수학점 범위 확인
            time.append(a)
        else : #학점 범위가 틀릴시 다시 입력
            print("다시입력하여주세요")
            a = float(input("{}학년 {}학기 이수학점을 입력하세요 :".format(i,n)))
            time.append(a)
        b = float(input("{}학년 {}학기 평점을 입력하세요 :".format(i,n)))
        if 0 <= b <= 4.5 : #제어문으로 평점 범위 확인
            grade.append(b)
        else : #학점 범위가 틀릴시 다시 입력
            print("다시입력하여주세요 ")
            b = float(input("{}학년 {}학기 평점을 입력하세요 :".format(i, n)))
            grade.append(b)
            
avg_grade = sum(grade) / len(grade) #평균 평점 구하는 거

print("총 이수학점 {}".format(sum(time)))
print("평균 평점 {}".format(avg_grade))

grade_ok()
