from turtle import Turtle,Screen
class Paddle:
    def __init__(self):
        self.new_paddle =Turtle()
        self.new_paddle.color("white")
        self.new_paddle.shape("square")
        self.new_paddle.shapesize(stretch_wid=5,stretch_len=1)
        # self.new_paddle.speed("fastest")

    def position(self,x_pos,y_pos):
        self.new_paddle.penup()
        self.new_paddle.goto(x_pos,y_pos)

    def up(self):
        new_y = self.new_paddle.ycor() + 20
        self.new_paddle.goto(self.new_paddle.xcor(),new_y)

    def down(self):
        new_y = self.new_paddle.ycor() - 20
        self.new_paddle.goto(self.new_paddle.xcor(), new_y)