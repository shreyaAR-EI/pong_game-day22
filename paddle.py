from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)


    def up(self):
        """makes the paddle move up by 20 pixels"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        """makes the paddle move down by 20 pixels"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)