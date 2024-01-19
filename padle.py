from turtle import Turtle


class Padle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.color("white")
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.setposition(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.setposition(self.xcor(),self.ycor() - 20)
