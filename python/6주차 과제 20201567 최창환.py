 #. 6주차 과제 20201567 최창환

#문제1. 다각형 그리기

import turtle as t

def 다각형(clr, n) :
    for i in range(n):
        t.color(clr)
        t.forward(120)
        t.left(360 / n)
        t.shape('turtle')



for a in range(1, 999999):
    n = int(input("그리고 싶은 다각형의 면의 갯수를 입력하세요 :"))
    if n == 0 :
        break
    clr = input("색상을 선택하세요:")
    다각형(clr, n)

print("다각형 그리기를 종료합니다.")
print("")

#문제2. 숭실카페의 음료 주문 시스템 만들기
c = ""
s = ""
result = []
r = []
#. 인사말
def hello() :
    print("숭실카페에 오신것을 환영합니다. ^^")
    print("커피 종류와 사이즈를 선택해 주세요.")
    
#.커피종류를 선택하면 그 가격이 리스트에 더해진다.
def coffee(c) :
    if c == "A" :
        result.append(3900)
    elif c == 'CM' :
        result.append(4500)
    elif c == 'CL' :
        result.append(5000)
    elif c == 'GT' :
        result.append(5500)
    return result

#.커피 사이즈를 선택하면 그 가격이 리스트에 더해진다.
def size(s) :
    if s == "G" :
        r.append(1000)
    elif s == 'R' :
        r.append(500) 
    elif s == 'S' :
        r.append(0)
    return r

#. 두 리스트의 합
def Price(c, s) :
    p = r.pop() + result.pop()
    print("총 금액은",p, "입니다." )
    return 

for i in range(1, 6) :
    hello()
    c = input("A(아메리카노) / CM(카페모카) / CL(카페라떼) / GT(그린티)  :")
    coffee(c)
    s = input("G(Grande) / R(Reguar) / S(Short) :")
    size(s)
    Price(c, s)
    print("맛있게 드세요~~")
    print(" ")

