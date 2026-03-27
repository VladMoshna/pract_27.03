import turtle as t
import random


t.speed(0)
t.width(3)

t.penup()
t.goto(100, -100)
t.pendown()
t.color("purple")
for _ in range(36):
    t.color(random.choice(["red", "green", "blue", "orange", "purple", "black"]))
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)


t.done()