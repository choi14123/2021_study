# 2주차 과제 20201567 최창환

# 문제 1. 원의 반지름과 길이
반지름 = 5.5
길이 = 12
넓이= 반지름 * 반지름 * 3.14
부피 = 넓이 * 길이
둘레 = 부피

# 문제 2. 파운드를 킬로그램으로 변환

a = int(input('파운드를 입력하세요:'))
b = a * 0.454
print('파운드의 양은',a, '킬로그램은', b,'킬로그램입니다.')


# 문제 3. 별 그리기

import turtle as t
t.shape('turtle')
t.shapesize(3)
for i in range(5):
    t.fd(300)
    t.lt(144)
    t.lt(72)
    t.fd(300)

# 문제 4. 계단 모양 그리기

import turtle as t
t.shape('turtle')
t.shapesize(2)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.rt(90)
