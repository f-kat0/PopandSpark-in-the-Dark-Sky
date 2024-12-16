import turtle


class Shooter:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("triangle")
        self.turtle.color("red")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(0, -270)
        self.turtle.setheading(90)

    def move_left(self):
        x = self.turtle.xcor() - 20
        if x > -380:
            self.turtle.setx(x)

    def move_right(self):
        x = self.turtle.xcor() + 20
        if x < 340:
            self.turtle.setx(x)

    def position(self):
        return self.turtle.xcor(), self.turtle.ycor()
