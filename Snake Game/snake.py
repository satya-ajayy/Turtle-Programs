from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE, UP, DOWN, LEFT, RIGHT = 20, 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        new_part = Turtle('circle')
        new_part.color('red')
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)

    def extend_length(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for part in range(len(self.segments)-1, 0, -1):
            self.segments[part].goto(self.segments[part-1].xcor(),
                                     self.segments[part-1].ycor())
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
