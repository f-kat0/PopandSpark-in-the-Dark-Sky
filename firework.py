import random
import turtle


class Firework:
    def __init__(self, x, y):
        self.particles = []
        for i in range(30):
            particle = turtle.Turtle()
            particle.shape("circle")
            particle.color(random.choice(["red", "yellow", "blue", "green", "purple", "orange", "white"]))
            particle.penup()
            particle.speed(0)
            particle.goto(x, y)
            particle.vx = random.uniform(-4, 4)
            particle.vy = random.uniform(-4, 4)
            particle.lifetime = random.randint(20, 50)
            self.particles.append(particle)

    def update(self):
        for particle in self.particles[:]:
            particle.setx(particle.xcor() + particle.vx)
            particle.sety(particle.ycor() + particle.vy)
            particle.lifetime -= 1
            particle.shapesize(stretch_wid=particle.shapesize()[0] * 0.9,
                               stretch_len=particle.shapesize()[1] * 0.9)
            if particle.lifetime <= 0:
                particle.hideturtle()
                self.particles.remove(particle)
