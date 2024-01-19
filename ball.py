from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.increment_x = 10
        self.increment_y = 10
        self.move_speed = 0.1
    def move(self):
        self.setposition(self.xcor()+ self.increment_x, self.ycor() + self.increment_y)

    def bounce_y(self):
        self.increment_y = - self.increment_y

    def bounce_x(self):
        self.increment_x = -self.increment_x
        self.move_speed *= 0.9
    def reset_l(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
    def reset_r(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1