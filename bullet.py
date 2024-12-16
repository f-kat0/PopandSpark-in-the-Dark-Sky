import turtle


class Bullet:
    def __init__(self, x, y):
        self.turtle = turtle.Turtle()
        self.turtle.shape("triangle")
        self.turtle.color("orange")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(x, y + 10)
        self.turtle.setheading(90)
        self.vx = 0
        self.vy = 15
        self.radius = 5
        self.turtle.shapesize(stretch_wid=0.5, stretch_len=1.5)

    def move(self):
        self.turtle.sety(self.turtle.ycor() + self.vy)

    def remove_off_screen(self):
        self.turtle.hideturtle()

    def position(self):
        return self.turtle.xcor(), self.turtle.ycor()
