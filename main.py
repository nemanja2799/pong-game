from turtle import Screen
from padle import Padle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Padle((350, 0))
l_paddle = Padle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect colision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_l()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_r()
        scoreboard.r_point()

screen.exitonclick()
