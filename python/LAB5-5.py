import turtle
t = turtle.Turtle()
t.shape("turtle")


s = turtle.textinput("", "몇각형을 원하시나요? : ")
d = turtle.textinput("", "한변의 길이를 어느정도 원하시나요? : ")
n = int(s)
m = int(d)

for i in range(n):
    t.forward(m)
    t.left(360/n)
