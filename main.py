from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("krsna's pong game")
screen.tracer(0)

paddle_rt = Paddle((350,0))
paddle_left = Paddle((-350,0))

screen.listen()
screen.onkeypress(key="Up", fun=paddle_rt.up)
screen.onkeypress(key="Down",fun=paddle_rt.down)
screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key="s",fun=paddle_left.down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()