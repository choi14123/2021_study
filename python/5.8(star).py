import turtle
t = turtle.Turtle()
t.shape("turtle")
i = 0
while i < 5 :
    t.forward(65)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(65)
    t.left(144)
    i = i + 1
