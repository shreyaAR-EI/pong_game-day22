from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("krsna's pong game")
screen.tracer(0)                                 # to pause the screen to not show generation and moving of the turtles

paddle_rt = Paddle((350,0))
paddle_left = Paddle((-350,0))
ball=Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_rt.up)
screen.onkeypress(key="Down",fun=paddle_rt.down)
screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key="s",fun=paddle_left.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)               # to  make the ball move at a slower speed to that we can catch it
    screen.update()                            # updates the screen everytime loop runs, to see the position of each elements
    ball.move()

    #detect collision with the up and down wall
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()

    #collision with paddle
    if ball.distance(paddle_rt) < 50 and ball.xcor() > 330 or ball.distance(paddle_left)<50 and ball.xcor() < -330:
        ball.bounce_x()

    #when ball is missed by rt paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # ball missed by left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()