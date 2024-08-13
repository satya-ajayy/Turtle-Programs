import turtle as t

t.pensize(2)
t.fillcolor('black')
t.begin_fill()
t.up()
t.goto(-40, -200)
t.down()
t.circle(180)
t.end_fill()

t.right(90)
pos = [(-100, 100), (-20, 100)]
for x, y in pos:
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor('red')
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()

t.up()
t.goto(-100, 100)
t.down()
t.left(22)
t.begin_fill()
for i in range(2):
    t.forward(217)
    t.left(68)
    t.forward(40)
    t.left(112)
t.end_fill()
t.mainloop()
