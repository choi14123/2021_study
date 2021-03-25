import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오 : ")
if s == "사각형" :
    s = turtle.textinput("", "가로: ")
    w = int(s)
    s = turtle.textinput("", "세로: ")
    h = int(s)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    
elif s == "삼각형" :
     s = turtle.textinput("", "밑변: ")
     a = int(s)
     t.forward(a)
     t.left(120)
     t.forward(a)
     t.left(120)
     t.forward(a)

elif s == "원" :
    s = turtle.textinput("", "반지름: ")
    r = int(s)
    t.circle(r)
     
turtle.done()
