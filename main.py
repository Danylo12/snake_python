import pygame
from game import Game

cell_size = 10
x_size = 50
y_size = 50

def run():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    game = Game(x_size, y_size, cell_size)
    game.run()


run()


