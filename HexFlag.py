import turtle
colors = ["green", "white", "red", "violet"]
t = turtle.Pen()
turtle.bgcolor("black")
for i in range(100):
    t.pencolor(colors[i % 3])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(256)
    t.speed(160)
