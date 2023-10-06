from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)

    def up_ar(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def dow_ar(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)