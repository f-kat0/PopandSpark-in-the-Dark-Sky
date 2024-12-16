from game import Game

# The player is able to adjust the number of balls and time limit here
num_balls = 10
time_limit = 60

game = Game(num_balls=num_balls, time_limit=time_limit)
game.run()
