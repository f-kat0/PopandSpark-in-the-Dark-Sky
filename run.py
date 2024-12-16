from game import Game

# The player is able to adjust the number of balls and time limit here
num_balls = 15
time_limit = 30

game = Game(num_balls=num_balls, time_limit=time_limit)
game.run()
