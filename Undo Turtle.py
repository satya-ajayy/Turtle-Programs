from turtle import Turtle, Screen, mainloop
from time import sleep


def Design(p, n, m):
    turtlelist = [p]
    for i in range(1, n):
        q = p.clone()
        q.rt(360.0 / n)
        turtlelist.append(q)
        p = q
    for i in range(n):
        c = abs(n / 2.0 - i) / (n * .7)
        for t in turtlelist:
            t.rt(360.0 / n)
            t.pencolor(1 - c, 0, c)
            t.fd(m)


def main():
    s = Screen()
    s.bgcolor('black')
    p = Turtle()
    p.speed(-1)
    p.hideturtle()
    p.pencolor('red')
    p.pensize(3)
    s.tracer(36, 0)
    Design(p, 36, 19)
    sleep(1)

    while any(t.undobufferentries() for t in s.turtles()):
        for t in s.turtles():
            t.undo()


if __name__ == '__main__':
    main()
    mainloop()
