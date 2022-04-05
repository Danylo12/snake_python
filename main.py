import pygame
import sys
import controls

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Snake Game")
    bg_color = (0, 0, 0)

    while True:
        screen.fill(bg_color)
        pygame.display.flip()
        controls.events()

run()

