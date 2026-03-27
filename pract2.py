import turtle as t


t.speed(0)
t.width(3)
t.penup()
t.goto(-200, -100)
t.pendown()

t.color("black")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.goto(-200, -100)
t.pendown()
t.color("orange")
t.begin_fill()
t.forward(100)
t.left(135)
t.forward(70)
t.left(90)
t.forward(70)
t.end_fill()
t.left(135)


t.done()