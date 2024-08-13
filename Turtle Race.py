from turtle import Turtle, Screen
from random import randint


def draw_Track():
    t = Turtle()
    pos = [-175, -125, -75, -25, 25, 75, 130, 175]
    t.penup()
    t.pensize(2)
    for ind in range(8):
        t.goto(-250, pos[ind])
        t.pendown()
        for _ in range(17):
            t.pendown()
            t.forward(15)
            t.penup()
            t.forward(15)
        t.penup()
    t.goto(235, -185)
    t.pencolor('red')
    t.left(90)
    t.pendown()
    t.forward(370)
    t.hideturtle()


is_started = False
screen = Screen()
screen.setup(width=600, height=400)
title = 'TURTLE RACE'
prompt = 'Enter Your Color ?'
choice = screen.textinput(title, prompt)
colors = ['aquamarine', 'gold', 'dark red',
          'salmon', 'indigo', 'dark green', 'gray']
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-235, y_positions[i])
    all_turtles.append(new_turtle)

if choice:
    is_started = True
    draw_Track()

while is_started:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_started = False
            winner_color = turtle.pencolor()
            if winner_color == choice:
                print(f"Yay! you and your {choice} turtle won the race.")
            else:
                print(f"Oops! Your {choice} turtle couldn't win the race.")
                print(f"The winner is {winner_color} turtle.")
        turtle.forward(randint(1, 10))
screen.exitonclick()
