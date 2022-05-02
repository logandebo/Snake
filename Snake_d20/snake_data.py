from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]


    def create_snake(self):
        x_cor = 0
        for i in range(3):
            new_part = Turtle(shape="square")
            new_part.color("white")
            new_part.penup()
            self.snake_parts.append(new_part)
            self.snake_parts[i].goto(x=x_cor, y=0)
            x_cor -= 20


    def move(self):
        for part_index in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_index - 1].xcor()
            new_y = self.snake_parts[part_index - 1].ycor()
            self.snake_parts[part_index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        self.snake_parts.append(new_part)
        self.snake_parts[-1].goto(self.snake_parts[-2].position())


    def reset(self):
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

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





