from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = .1
        self.speed('fastest')

    def move(self):
        nex_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(nex_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= .9
    def bounce_x(self):
        self.x_move *=-1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = .1