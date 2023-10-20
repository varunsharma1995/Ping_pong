import turtle
from turtle import Turtle, Screen
from paddle import Paddle, Dashline
from ball import Ball
from scoreBoard import Scoreboard
import time
dashline = Dashline()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move(10, 10)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()
    if ball.xcor() < - 380:
        ball.reset_position()
        score.l_point()

    # if ball.xcor() >330 or ball.xcor()< -330:
    #     score.score_calculator(ball,r_paddle,l_paddle)
    #     screen.update()
    #     game_is_on =False

screen.exitonclick()
