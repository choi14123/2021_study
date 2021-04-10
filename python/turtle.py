import turtle
import turtle as t
def drawBar (height) :
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

data = [120, 140, 70, 65, 200, 25, 100]
t = turtle.Turtle()
t.color("green")
t.fillcolor("red")
t.pensize(4)

for d in data :
    drawBar(d)
t.left(180)
t.forward(280)
