import turtle as t


t.speed(0)
t.width(3)

t.color("red")
t.penup()
t.goto(-250, 100)
t.pendown()
for _ in range(4):
    t.forward(80)
    t.right(90)

t.color("green")
t.penup()
t.goto(-100, 100)
t.pendown()
for _ in range(3):
    t.forward(80)
    t.right(120)

t.color("blue")
t.penup()
t.goto(80, 100)
t.pendown()
for _ in range(5):
    t.forward(80)
    t.right(72)


t.done()