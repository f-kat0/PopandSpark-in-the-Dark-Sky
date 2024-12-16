import turtle
import random


class Background:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Interactive Fireworks with OOP")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def listen(self):
        self.screen.listen()

    def draw_star(self, x, y, size=5):
        star = turtle.Turtle()
        star.hideturtle()
        star.penup()
        star.goto(x, y)
        star.pendown()
        star.color("white")
        star.begin_fill()
        for i in range(5):
            star.forward(size)
            star.right(144)
        star.end_fill()

    def add_stars(self, count=20):
        """Adds multiple stars at random positions."""
        for _ in range(count):
            x = random.randint(-400, 350)
            y = random.randint(-250, 270)
            size = random.randint(1, 7) * 2  
            self.draw_star(x, y, size)

    def draw_moon(self):
        """Draws a crescent moon."""
        moon = turtle.Turtle()
        moon.hideturtle()

        moon.penup()
        moon.goto(-300, 170)
        moon.pendown()
        moon.color("white")
        moon.begin_fill()
        moon.circle(40)
        moon.end_fill()

        moon.penup()
        moon.goto(-280, 170)
        moon.pendown()
        moon.color("black")
        moon.begin_fill()
        moon.circle(40)
        moon.end_fill()


class Frame:
    def __init__(self):
        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.color("white")
        self.draw()

    def draw(self):
        self.drawer.penup()
        self.drawer.goto(-400, 300)
        self.drawer.pendown()
        self.drawer.pensize(3)
        for i in range(2):
            self.drawer.forward(800)
            self.drawer.right(90)
            self.drawer.forward(600)
            self.drawer.right(90)
