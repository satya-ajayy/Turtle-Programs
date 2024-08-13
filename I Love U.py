import turtle as t

t.speed('fastest')
t.bgcolor('black')
t.width(12)


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


def heart():
    t.color('red', 'red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()


def main():
    heart()
    t.penup()
    t.goto(-300, -20)
    t.pencolor('red')
    t.write('I   U', align='left', font=('courier new', 150, 'bold'))
    t.mainloop()

    
main()
