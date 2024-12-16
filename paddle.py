import turtle


class Paddle:
    def __init__(self, shooter):
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.shapesize(stretch_wid=1, stretch_len=5)
        self.turtle.goto(0, -240)
        self.shooter = shooter

    def move(self):
        shooter_x, _ = self.shooter.position()
        paddle_x = self.turtle.xcor()

        if shooter_x > paddle_x:
            self.turtle.setx(min(shooter_x, 330))
        elif shooter_x < paddle_x:
            self.turtle.setx(max(shooter_x, -380))

    def position(self):
        return self.turtle.xcor(), self.turtle.ycor()
