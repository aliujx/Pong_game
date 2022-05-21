from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.listen()
screen.tracer(0)

gamer_1 = Paddle((-360, 0))
gamer_2 = Paddle((360, 0))

screen.update()
gamer_1.showturtle()
gamer_2.showturtle()

screen.onkey(gamer_2.go_up, "Up")
screen.onkey(gamer_2.go_down, "Down")

screen.onkey(gamer_1.go_up, "a")
screen.onkey(gamer_1.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    if ball.distance(gamer_2) <= 50 and ball.xcor() > 330 or ball.distance(gamer_1) <= 50 and ball.xcor() < -330:
        ball.paddle_bounce()
    if ball.xcor() > 380:
        time.sleep(1)
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        time.sleep(1)
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
