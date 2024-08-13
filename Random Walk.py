import turtle as t
from random import choice


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"
           , "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
t.pensize(10)
t.speed(0)

for _ in range(200):
    t.color(choice(colours))
    t.forward(30)
    t.setheading(choice(directions))

t.exitonclick()
