import pygame, sys
import controls, os
import turn, Snake

# appending instances to list
# list.append( geeks('Akash', 2) )
# list.append( geeks('Deependra', 40) )
# list.append( geeks('Reaper', 44) )

grass_img = pygame.image.load('assets/empty.png')
list_of_turns = []
bg = pygame.image.load(os.path.join("assets", "empty.png"))
snake_head=pygame.image.load('assets/snake_head.png')


def run():
    pygame.init()
    screen = pygame.display.set_mode((650, 450))
    snake_head_top = screen.get_height() - snake_head.get_height()
    pygame.display.set_caption("Snake Game")
#    bg_color = (0, 0, 0)

    while True:
        screen.fill([255, 255, 255])
#        screen.blit(bg, (0, 0))
        screen.blit(bg, (120, 440))
        for y in range(0, 440, 60):
            for x in range(0, 640, 60):
                screen.blit(bg, (x, y))
        x, y = pygame.mouse.get_pos()
        screen.blit(snake_head, (x - snake_head.get_width() / 2, snake_head_top))
        pygame.display.flip()
        controls.events()

run()

