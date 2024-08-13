import turtle as t

colors = ["cornflower blue", "aquamarine", "gold", "dark red",
          "salmon", "indigo", "dark green", "gray"]


def draw_shapes(n):
    for _ in range(n):
        t.forward(100)
        t.right(360//n)


t.pensize(10)
t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(25)
t.right(90)
t.right(90)
t.pendown()
for i in range(3, 9):
    t.color(colors[i - 3])
    draw_shapes(i)
t.exitonclick()
