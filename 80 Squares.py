import turtle as t
import random as rd

t.bgcolor("black")
t.speed(0)


def draw_square():
    colors = ["red", "blue", "orange", "green", "purple", "skyblue", "yellow", "white"]
    colour = rd.choice(colors)
    t.pencolor(colour)
    for side in range(4):
        t.forward(100)
        t.right(90)
        for i in range(4):
            t.forward(50)
            t.right(90)


t.penup()
t.back(20)
t.pendown()
for square in range(80):
    draw_square()
    t.forward(5)
    t.left(5)
t.hideturtle()
t.mainloop()
