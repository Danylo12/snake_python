import random

import pygame, sys
import controls, os
from Snake import Snake
from Food import Apple
import time

# appending instances to list
# list.append( geeks('Akash', 2) )
# list.append( geeks('Deependra', 40) )
# list.append( geeks('Reaper', 44) )

grass_img = pygame.image.load('assets/empty.png')
list_of_turns = []
bg = pygame.image.load(os.path.join("assets", "empty.png"))
length = 0
head_y = 0
head_x = 0
image = pygame.image.load(os.path.join('assets', 'snake_head.png'))
image_food = pygame.image.load(os.path.join('assets', 'apple.png'))
space_size = 50
Game_Height = 450
Game_width = 650

#def eat_food(screen):
#    food_x = random.randint(0, 640)
#    food_y = random.randint(0, 440)
#    screen.blit(image_food, (food_x, food_y))

def is_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + space_size:
        if y1 >= y2 and y1 < y2 + space_size:
            return True
    return False

def play(snake, apple):
        snake.output()
        snake.update()
        apple.draw()
        pygame.display.flip()

        if is_collision(snake.rect.centerx, snake.rect.centery, apple.x, apple.y):
            apple.move()


def run():
    pygame.init()
    screen = pygame.display.set_mode((Game_width, Game_Height))
    pygame.display.set_caption("Snake Game")
    snake = Snake(screen, length, list_of_turns, image)
    apple = Apple(screen)

#    food_x = random.randint(0, 640)
#    food_y = random.randint(0, 440)
#    screen.blit(image_food, (food_x, food_y))



    while True:
        for y in range(0, Game_Height, 60):
            for x in range(0, Game_width, 60):
                screen.blit(bg, (x, y))
        controls.events(snake, 10)
        play(snake, apple)



run()


