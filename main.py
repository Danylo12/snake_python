import pygame, sys
import controls
import turn
# appending instances to list
# list.append( geeks('Akash', 2) )
# list.append( geeks('Deependra', 40) )
# list.append( geeks('Reaper', 44) )

list_of_turns = []

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

