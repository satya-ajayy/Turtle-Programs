import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n, h = 36, 0
for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1 / n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(200)
        t.left(150)
turtle.mainloop()
