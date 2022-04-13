import pygame, sys

def events(snake, space_size):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.mdown = False
                snake.mup = False
                snake.mleft = False
                snake.mright = True
            if event.key == pygame.K_LEFT:
                snake.mup = False
                snake.mdown = False
                snake.mright = False
                snake.mleft = True
            if event.key == pygame.K_UP:
                snake.mup = True
                snake.mdown = False
                snake.mright = False
                snake.mleft = False
            if event.key == pygame.K_DOWN:
                snake.mup = False
                snake.mdown = True
                snake.mright = False
                snake.mleft = False


