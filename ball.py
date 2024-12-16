import random
import math
import turtle


class Ball:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(random.choice(["purple", "hotpink", "orange", "yellow", "blue"]))
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(random.randint(-300, 300), random.randint(-200, 200))
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.radius = 10

    def move(self):
        x, y = self.turtle.xcor(), self.turtle.ycor()
        self.turtle.setx(x + self.vx) 
        self.turtle.sety(y + self.vy)

        if x + self.vx > 390 or x + self.vx < -390:
            self.vx = -self.vx
        if y + self.vy > 290 or y + self.vy < -290:
            self.vy = -self.vy

    def position(self):
        return self.turtle.xcor(), self.turtle.ycor()

    def remove_off_screen(self):
        self.turtle.hideturtle() 

    def check_bounce_off(self, other):
        x1, y1 = self.position()
        x2, y2 = other.position()
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return d < (self.radius + other.radius)

    def bounce_off(self, other):
        x1, y1 = self.position()
        x2, y2 = other.position()
        dx = x2 - x1
        dy = y2 - y1
        dist = math.sqrt(dx ** 2 + dy ** 2)

        nx = dx / dist
        ny = dy / dist

        dvx = other.vx - self.vx
        dvy = other.vy - self.vy

        dot_product = dvx * nx + dvy * ny

        if dot_product > 0:
            return

        self.vx = -self.vx
        self.vy = -self.vy
        other.vx = -other.vx
        other.vy = -other.vy

    def check_bounce_paddle(self, paddle):
        ball_x, ball_y = self.turtle.xcor(), self.turtle.ycor()
        paddle_x, paddle_y = paddle.turtle.xcor(), paddle.turtle.ycor()

        if (ball_y - self.radius <= paddle_y + 10) and (ball_y - self.radius >= paddle_y - 10):
            if paddle_x - 50 <= ball_x <= paddle_x + 50:
                return True
        return False

    def bounce_paddle(self, paddle):
        self.vy = -self.vy
        self.turtle.sety(paddle.turtle.ycor() + 10 + self.radius)
