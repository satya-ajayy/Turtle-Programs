import math as m
import turtle as t


def sine(x):
    return 15 * m.sin(x) ** 3


def cose(x):
    return 12 * m.cos(x) - 5 * m.cos(2 * x)\
        - 2 * m.cos(3 * x) - m.cos(4 * x)


t.speed('fastest')
t.bgcolor('black')
for i in range(6000):
    t.goto(sine(i) * 20, cose(i) * 20)
    for j in range(5):
        t.color('red')
    t.goto(0, 0)
t.done()
