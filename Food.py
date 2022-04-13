import pygame
from controls import events
import random
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("assets/apple.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        space_size = 50
        self.x = random.randint(1,12)*space_size
        print(self.x)
        self.y = random.randint(1,8)*space_size
        print(self.y)

