import turtle as t

t.bgcolor("black")
colors = ("red", "blue", "orange", "green", "purple", "skyblue", "yellow", "white")
t.speed(0)
x = 30
y = 0
while True:
    t.circle(x)
    t.pencolor(colors[y % 8])
    t.forward(x)
    t.right(45)
    x += 0.5
    y += 1
    if x == 100:
        break
t.mainloop()
