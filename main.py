from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("krsna's pong game")

paddle_rt = Paddle()
paddle_rt.position(x_pos=350,y_pos=0)
screen.listen()
screen.onkey(key="Up", fun=paddle_rt.up)
screen.onkey(key="Down",fun=paddle_rt.down)

screen.exitonclick()