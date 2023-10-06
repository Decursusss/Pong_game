import random
import time
import turtle
import move
import ball
import score
from turtle import Turtle

screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = move.Paddle(350,0)
l_paddle = move.Paddle(-350,0)
game_ball = ball.Ball()
scoreboard = score.Scoreboard()


screen.listen()
screen.onkey(r_paddle.up_ar, "Up")
screen.onkey(r_paddle.dow_ar, "Down")
screen.onkey(l_paddle.up_ar, "w")
screen.onkey(l_paddle.dow_ar, "s")


game_is_on = True
while game_is_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()

    if  game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce()

    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_padle()

    if game_ball.xcor() > 380:
        game_ball.restart()
        scoreboard.score_l()

    if game_ball.xcor() < -380:
        game_ball.restart()
        scoreboard.score_r()

screen.exitonclick()