import time
import turtle
from bg import Background, Frame
from ball import Ball
from shooter import Shooter
from bullet import Bullet
from firework import Firework
from paddle import Paddle


class Game:
    def __init__(self, num_balls=10, time_limit=60):
        self.bg = Background()
        self.frame = Frame()
        self.shooter = Shooter()
        self.paddle = Paddle(self.shooter)
        self.num_balls = [Ball() for i in range(num_balls)]
        self.num_bullets = []
        self.num_fireworks = []
        self.time_limit = time_limit
        self.time_left = self.time_limit
        self.time_start = time.time()
        self.game_win = False

        self.balls_left_display = self.set_display(-380, 260,
                                                   f"Remaining Balls: {len(self.num_balls)}")
        self.time_display = self.set_display(210, 260,
                                             f"Remaining Time: {self.time_left}")

        self.set_control()
        self.update_time()
        self.set_scene()

    def set_scene(self):
        self.bg.draw_moon()
        self.bg.add_stars(30)
        self.bg.update()

    def set_display(self, x, y, text):
        display = turtle.Turtle()
        display.hideturtle()
        display.color("white")
        display.penup()
        display.goto(x, y)
        display.write(text, font=("Trebuchet MS", 20, "normal"))
        return display

    def set_control(self):
        self.bg.screen.onkeypress(self.shooter.move_left, "Left")
        self.bg.screen.onkeypress(self.shooter.move_right, "Right")
        self.bg.screen.onkeypress(self.shoot, "space")
        self.bg.listen()

    def shoot(self):
        if len(self.num_bullets) < 5:
            x, y = self.shooter.position()
            self.num_bullets.append(Bullet(x, y))

    def update_time(self):
        if self.time_left > 0 and not self.game_win:
            self.time_left -= 1
            self.time_display.clear()
            self.time_display.write(f"Remaining Time: {self.time_left}",
                                    font=("Trebuchet MS", 20, "normal"))
            self.bg.screen.ontimer(self.update_time, 1000)
        elif not self.game_win:
            self.lose()

    def move(self):
        self.paddle.move()
        for ball in self.num_balls:
            ball.move()
            if ball.check_bounce_paddle(self.paddle):
                ball.bounce_paddle(self.paddle)

        for bullet in self.num_bullets[:]:
            bullet.move()
            if bullet.position()[1] > 300:
                bullet.remove_off_screen()
                self.num_bullets.remove(bullet)

        for firework in self.num_fireworks[:]:
            firework.update()
            if not firework.particles:
                self.num_fireworks.remove(firework)

    def check_win(self):
        for ball in self.num_balls[:]:
            for bullet in self.num_bullets[:]:
                if ball.check_bounce_off(bullet):
                    x, y = ball.position()
                    self.num_fireworks.append(Firework(x, y))
                    ball.remove_off_screen()
                    bullet.remove_off_screen()
                    self.num_balls.remove(ball)
                    self.num_bullets.remove(bullet)
                    self.update_balls_left()

        for i in range(len(self.num_balls)):
            for j in range(i + 1, len(self.num_balls)):
                if self.num_balls[i].check_bounce_off(self.num_balls[j]):
                    self.num_balls[i].bounce_off(self.num_balls[j])

        if not self.num_balls and not self.game_win:
            self.game_win = True
            self.win()

    def update_balls_left(self):
        self.balls_left_display.clear()
        self.balls_left_display.write(f"Remaining Balls: {len(self.num_balls)}",
                                      font=("Trebuchet MS", 20, "normal"))

    def win(self):
        win = turtle.Turtle()
        win.hideturtle()
        win.color("green")
        win.penup()
        win.goto(0, 0)
        win.write(" YOU WIN!🏆", align="center", font=("Comic Sans MS", 40, "bold"))
        win.goto(0, -30)
        time_taken = time.time() - self.time_start
        win.color("white")
        win.write(f"Time Taken: {time_taken:.2f} seconds",
                  align="center", font=("Courier", 20, "normal"))
        self.bg.update()

    def lose(self):
        lose = turtle.Turtle()
        lose.hideturtle()
        lose.color("red")
        lose.penup()
        lose.goto(0, 0)
        lose.write("GAME OVER!😢", align="center", font=("Comic Sans MS", 40, "bold"))
        lose.goto(0, -30)
        lose.color("white")
        lose.write(f"Remaining Balls: {len(self.num_balls)}",
                   align="center", font=("Courier", 20, "normal"))
        self.bg.update()

    def run(self):
        while self.time_left > 0 and not self.game_win:
            self.move()
            self.check_win()
            self.bg.update()
        turtle.done()
